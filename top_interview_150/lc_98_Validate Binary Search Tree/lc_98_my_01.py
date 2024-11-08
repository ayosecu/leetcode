# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """       
        def myDfs(node):
            if node:
                if node.left and node.left.val >= node.val:
                    return False
                if node.right and node.right.val <= node.val:
                    return False

            if node.left:
                if not myDfs(node.left):
                    return False

                most_right = node.left
                while most_right.right:
                    most_right = most_right.right
                if most_right.val >= node.val:
                    return False

            if node.right:
                if not myDfs(node.right):
                    return False
                most_left = node.right
                while most_left.left:
                    most_left = most_left.left
                if most_left.val <= node.val:
                    return False

            return True
        
        return myDfs(root)

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