# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        current = root
        st = [] # Stack
        count = 0

        while st or current:
            while current:
                st.append(current)
                current = current.left
            pop_node = st.pop()
            count += 1
            if count == k:
                return pop_node.val
            if pop_node.right:
                current = pop_node.right

        return None

def test_kth_smallest():
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)  
    result1 = sol.kthSmallest(root1, 1)
    assert result1 == 1, "TC1 - Expected: {}, Result: {}".format(1, result1)

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.left.left = TreeNode(1)
    root2.left.right = TreeNode(4)  
    result2 = sol.kthSmallest(root2, 3)
    assert result2 == 3, "TC2 - Expected: {}, Result: {}".format(3, result2)

test_kth_smallest()