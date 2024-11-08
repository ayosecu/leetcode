from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        dq = deque([root])
        ret = []

        while dq:
            level_list = []
            for _ in range(len(dq)):
                pop_node = dq.popleft()
                level_list.append(pop_node.val)
                if pop_node.left:
                    dq.append(pop_node.left)
                if pop_node.right:
                    dq.append(pop_node.right)
            ret.append(level_list)

        return ret    

def doTest():
    sol = Solution()

    tc1 = TreeNode(3)
    tc1.left = TreeNode(9)
    tc1.right = TreeNode(20)
    tc1.right.left = TreeNode(15)
    tc1.right.right = TreeNode(7)
    expected = [[3], [9,20], [15,7]]
    result = sol.levelOrder(tc1)
    assert result == expected, "TC 1 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 1 Passed!")

    tc2 = TreeNode(1)
    expected = [[1]]
    result = sol.levelOrder(tc2)
    assert result == expected, "TC 2 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 2 Passed!")

    expected = []
    result = sol.levelOrder(None)
    assert result == expected, "TC 3 Failed - Expected: {}, Result: {}".format(expected, result)
    print("TC 3 Passed!")

doTest()