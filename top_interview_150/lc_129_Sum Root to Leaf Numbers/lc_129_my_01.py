# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.total = 0

    def sumNumbersMy(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(path, node):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                self.total += int("".join(path))
                path.pop()
                return
            
            dfs(path, node.left)
            dfs(path, node.right)          
            path.pop()

        dfs([], root)

        return self.total

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum
            
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)

def create_tree(values):
    """Helper function to create a binary tree from a list of values (level-order traversal)."""
    if not values:
        return None

    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

def run_tests():
    # Test cases
    test_cases = [
        ([1, 2, 3], 25),                      # Tree: [1, 2, 3], Paths: 12, 13
        ([4, 9, 0, 5, 1], 1026),              # Tree: [4, 9, 0, 5, 1], Paths: 495, 491, 40
        ([], 0),                              # Empty tree
        ([1], 1),                             # Single node
        ([1, 2], 12),                         # Left-skewed tree
        ([1, None, 3], 13),                   # Right-skewed tree
    ]

    for i, (values, expected) in enumerate(test_cases, 1):
        solution = Solution()
        root = create_tree(values)
        result = solution.sumNumbers(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()