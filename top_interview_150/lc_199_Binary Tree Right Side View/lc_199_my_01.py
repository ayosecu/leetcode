from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """      
        if root is None:
            return []
        
        result = []
        dq = deque([(root, 0)])   # (node, level)

        while dq:
            pop_node, level = dq.popleft()
            if len(dq) == 0:
                result.append(pop_node.val)
            else:
                front_level = dq[0][1]
                if front_level > level:
                    result.append(pop_node.val)
            if pop_node.left:
                dq.append((pop_node.left, level+1))
            if pop_node.right:
                dq.append((pop_node.right, level+1))

        return result

def doTest():
    sol = Solution()
    test1 = TreeNode(1)
    test1.left = TreeNode(2)
    test1.right = TreeNode(3)
    test1.left.right = TreeNode(5)
    test1.right.right = TreeNode(4)
    result1 = sol.rightSideView(test1)
    expected1 = [1, 3, 4]
    assert result1 == expected1, "TC1 - Test Failed. Expected: {}, Result: {}".format(expected1, result1)
    print(result1)

    test2 = TreeNode(1)
    test2.right = TreeNode(3)
    result2 = sol.rightSideView(test2)
    expected2 = [1, 3]
    assert result2 == expected2, "TC2 - Test Failed. Expected: {}, Result: {}".format(expected2, result2)
    print(result2)

    test3 = TreeNode(1)
    test3.left = TreeNode(2)
    result3 = sol.rightSideView(test3)
    expected3 = [1, 2]
    assert result3 == expected3, "TC3 - Test Failed. Expected: {}, Result: {}".format(expected3, result3)
    print(result3)

doTest()