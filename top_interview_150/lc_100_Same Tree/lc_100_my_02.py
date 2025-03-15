from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time complexity: O(n), n = The number of nodes
        - Space complexity: O(H), H = The height of tree.
            - Skewed Tree: H = n
            - Balanced Tree: H = logn
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True    
        elif not p or not q or p.val != q.val:
            return False                 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# TC
def test_isSameTree():
    sol = Solution()

    # Test case 1: Same
    print("test1")
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p, q) == True, "Test case 1 failed"
    
    # Test case 2: Different
    print("test2")
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p, q) == False, "Test case 2 failed"
    
    # Test case 3: Different
    print("test3")
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert sol.isSameTree(p, q) == False, "Test case 3 failed"
    
    # Test case 4: Empty
    print("test4")    
    p = None
    q = None
    assert sol.isSameTree(p, q) == True, "Test case 4 failed"

    # Test case 5: Different
    print("test5")    
    p = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p, q) == False, "Test case 5 failed"

    print("All test cases passed.")

# Test Execute
test_isSameTree()   
