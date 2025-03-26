from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes.
        - Space Complexity: O(H), H = The height of tree, skewed = O(n), balanced = O(logn)
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Visit inorder and check previous value and current value
        min_diff = float("inf")
        prev = None

        def inOrder(node):
            nonlocal min_diff, prev

            if not node:
                return
            
            inOrder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            inOrder(node.right)
        
        inOrder(root)
        return min_diff

def run_test():
    # TC 1: [4, 2, 6, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 1 - Expected: 1, Result:", result)

    # TC 2: [1, 0, 48, None, None, 12, 49]    
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(48)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(49)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 2 - Expected: 1, Result:", result)

    # TC 3: [236, 104, 701, None, 227, None, 911]
    root = TreeNode(236)
    root.left = TreeNode(104)
    root.right = TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 3 - Expected: 9, Result:", result)

run_test()