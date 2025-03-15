from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Time Complexity: O(n), n = The number of nodes
        Space Complexity: O(H), H = The height of tree
            - Skewed tree: H = n
            - Balanced tree: H = logn
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap left and right child
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

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
    print("TC1 Passed!")

    test2 = TreeNode(1)
    test2.left = TreeNode(2)
    result2 = printTree(sol.invertTree(test2))
    expected2 = [1, 2]
    assert result2 == expected2, "TC2 - Expected: {}, Result: {}".format(expected2, result2)
    print("TC2 Passed!") 

doTest()