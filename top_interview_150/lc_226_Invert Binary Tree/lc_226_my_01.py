from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        def inOrderDfs(node):
            if node is None:
                return           
            tmp = node.left
            node.left = node.right
            node.right = tmp
            inOrderDfs(node.left)
            inOrderDfs(node.right)
                    
        inOrderDfs(root)

        return root

def printTree(root):
    result = []

    if root is None:
        return result
    
    dq = deque([root])
    while dq:
        for _ in range(len(dq)):
            pop_node = dq.popleft()
            result.append(pop_node.val)
            if pop_node.left:
                dq.append(pop_node.left)
            if pop_node.right:
                dq.append(pop_node.right)
    
    return result

def doTest():
    sol = Solution()

    test1 = TreeNode(4)
    test1.left = TreeNode(2)
    test1.right = TreeNode(7)
    test1.left.left = TreeNode(1)
    test1.left.right = TreeNode(3)
    test1.right.left = TreeNode(6)
    test1.right.right = TreeNode(9)
    result1 = printTree(sol.invertTree(test1))
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    assert result1 == expected1, "TC1 - Expected: {}, Result: {}".format(expected1, result1)
    print(result1)

    test2 = TreeNode(1)
    test2.left = TreeNode(2)
    result2 = printTree(sol.invertTree(test2))
    expected2 = [1, 2]
    assert result2 == expected2, "TC2 - Expected: {}, Result: {}".format(expected2, result2)
    print(result2) 

doTest()
        