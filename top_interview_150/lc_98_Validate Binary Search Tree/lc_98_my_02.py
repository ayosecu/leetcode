from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check value comparing with min/max
        """
            - Time Complexity: O(n), n = the number of nodes
            - Space Complexity: O(H), H = height of Tree
                - Balanced Tree: O(logn)
                - Skewed Tree: O(n)
        """
        def checkVal(node, min, max):
            if not node:
                return True
            
            if node.val <= min or node.val >= max:
                return False
                        
            return checkVal(node.left, min, node.val) and checkVal(node.right, node.val, max)
        
        return checkVal(root, float("-inf"), float("inf"))


def doTest():
    sol = Solution()

    tc1 = TreeNode(2)
    tc1.left = TreeNode(1)
    tc1.right = TreeNode(3)
    expected = True
    result = sol.isValidBST(tc1)
    assert result == expected, "TC 1 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 1 Passed!!")

    tc2 = TreeNode(5)
    tc2.left = TreeNode(1)
    tc2.right = TreeNode(4)
    tc2.right.left = TreeNode(3)
    tc2.right.right = TreeNode(6)
    expected = False
    result = sol.isValidBST(tc2)
    assert result == expected, "TC 2 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 2 Passed!!")

    tc3 = TreeNode(5)
    tc3.left = TreeNode(4)
    tc3.right = TreeNode(6)
    tc3.right.left = TreeNode(3)
    tc3.right.right = TreeNode(7)
    expected = False
    result = sol.isValidBST(tc3)
    assert result == expected, "TC 3 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 3 Passed!!")

doTest()