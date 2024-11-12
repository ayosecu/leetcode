# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def makeNode(node, c, n):
            i, j = c[0], c[1]
            if n == 1:
                node.isLeaf = True
                node.val = grid[i][j]
                return

            total_sum = 0
            for k in range(n):
                sub_sum = 0
                for l in range(n):
                    sub_sum += grid[i+k][j+l]                            
                total_sum += sub_sum

            if  0 < total_sum < n * n:
                node.isLeaf = False
                half = n // 2
                node.topLeft = Node()
                makeNode(node.topLeft, (i, j), half)
                node.topRight = Node()
                makeNode(node.topRight, (i, j + half), half)
                node.bottomLeft = Node()
                makeNode(node.bottomLeft, (i + half, j), half)
                node.bottomRight = Node()
                makeNode(node.bottomRight, (i + half, j + half), half)
            else:
                node.isLeaf = True
                node.val = 0 if not total_sum else 1

        root = Node()       
        makeNode(root, (0, 0), len(grid))

        return root
        
def print_quad_tree(node):
    if node.isLeaf:
        return f"Leaf(val={node.val})"
    return (
        f"Node(val={node.val}, "
        f"topLeft={print_quad_tree(node.topLeft)}, "
        f"topRight={print_quad_tree(node.topRight)}, "
        f"bottomLeft={print_quad_tree(node.bottomLeft)}, "
        f"bottomRight={print_quad_tree(node.bottomRight)})"
    )

def run_tests():
    solution = Solution()

    # Test case 1: 2x2 uniform grid with all values 1
    grid1 = [
        [1, 1],
        [1, 1]
    ]
    result1 = solution.construct(grid1)
    expected1 = "Leaf(val=1)"
    result1_str = print_quad_tree(result1)
    print(f"Test 1 {'passed' if result1_str == expected1 else 'failed'}: Expected {expected1}, Got {result1_str}")

    # Test case 2: 2x2 uniform grid with all values 0
    grid2 = [
        [0, 0],
        [0, 0]
    ]
    result2 = solution.construct(grid2)
    expected2 = "Leaf(val=0)"
    result2_str = print_quad_tree(result2)
    print(f"Test 2 {'passed' if result2_str == expected2 else 'failed'}: Expected {expected2}, Got {result2_str}")

    # Test case 3: 2x2 non-uniform grid
    grid3 = [
        [1, 0],
        [0, 1]
    ]
    result3 = solution.construct(grid3)
    expected3 = "Node(val=False, topLeft=Leaf(val=1), topRight=Leaf(val=0), bottomLeft=Leaf(val=0), bottomRight=Leaf(val=1))"
    result3_str = print_quad_tree(result3)
    print(f"Test 3 {'passed' if result3_str == expected3 else 'failed'}: Expected {expected3}, Got {result3_str}")

    # Test case 4: 4x4 uniform grid
    grid4 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    result4 = solution.construct(grid4)
    expected4 = "Leaf(val=1)"
    result4_str = print_quad_tree(result4)
    print(f"Test 4 {'passed' if result4_str == expected4 else 'failed'}: Expected {expected4}, Got {result4_str}")

    # Test case 5: 4x4 non-uniform grid
    grid5 = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    result5 = solution.construct(grid5)
    expected5 = ("Node(val=False, topLeft=Leaf(val=1), topRight=Leaf(val=0), "
                 "bottomLeft=Leaf(val=0), bottomRight=Leaf(val=1))")
    result5_str = print_quad_tree(result5)
    print(f"Test 5 {'passed' if result5_str == expected5 else 'failed'}: Expected {expected5}, Got {result5_str}")

# Run the tests
run_tests()