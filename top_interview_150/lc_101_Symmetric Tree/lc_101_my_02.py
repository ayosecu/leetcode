from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(N), N = The number of nodes
        - Space Complexity: O(H), H = The height of tree
            - Skewed Tree: H = N
            - Balanced Tree: H = logN
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # check mirror: compare left child and right child
        def checkMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return checkMirror(node1.left, node2.right) and checkMirror(node1.right, node2.left)
        
        return checkMirror(root.left, root.right)

def run_tests():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    expected1 = True
    result1 = solution.isSymmetric(root1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    expected2 = False
    result2 = solution.isSymmetric(root2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    root3 = None

    expected3 = True
    result3 = solution.isSymmetric(root3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    root4 = TreeNode(1)

    expected4 = True
    result4 = solution.isSymmetric(root4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)

    expected5 = False
    result5 = solution.isSymmetric(root5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()