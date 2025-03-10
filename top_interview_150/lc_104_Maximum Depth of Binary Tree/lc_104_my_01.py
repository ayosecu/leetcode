# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        maxL = self.maxDepth(root.left)
        maxR = self.maxDepth(root.right)
        return max(maxL, maxR)+1

def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp
        if root is not None:
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


tc = [
        [3,9,20,None,None,15,7],
        [1,None,2],
        [],
        [1, 2, 3, 4, None, None, 5]
]

for t in tc:
    root = insert_level_order(t, None, 0, len(t))
    print(Solution().maxDepth(root))