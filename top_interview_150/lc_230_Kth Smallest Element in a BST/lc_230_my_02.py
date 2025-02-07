from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes
        - Space Complexity: O(n), n = The number of nodes
        - Note
            - If balanced: time complexity is O(logn), space complexity is O(n)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visit = []

        def inorder(node):
            if len(visit) >= k or not node:
                return
            
            inorder(node.left)
            if len(visit) < k:
                visit.append(node)
            inorder(node.right)

        inorder(root)

        return visit[-1].val

def test_kth_smallest():
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)  
    result1 = sol.kthSmallest(root1, 1)
    assert result1 == 1, "TC1 - Expected: {}, Result: {}".format(1, result1)
    print("TC1 Passed!!")

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.left.left = TreeNode(1)
    root2.left.right = TreeNode(4)  
    result2 = sol.kthSmallest(root2, 3)
    assert result2 == 3, "TC2 - Expected: {}, Result: {}".format(3, result2)
    print("TC2 Passed!!")

test_kth_smallest()            

        