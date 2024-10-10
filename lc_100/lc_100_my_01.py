# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 테스트 케이스들
def test_isSameTree():
    sol = Solution()

    # Test case 1: 같은 구조와 같은 값을 가지는 트리
    print("test1")
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p, q) == True, "Test case 1 failed"
    
    # Test case 2: 다른 구조를 가지는 트리
    print("test2")
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p, q) == False, "Test case 2 failed"
    
    # Test case 3: 같은 구조지만 다른 값을 가지는 트리
    print("test3")
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert sol.isSameTree(p, q) == False, "Test case 3 failed"
    
    # Test case 4: 둘 다 빈 트리
    print("test4")    
    p = None
    q = None
    assert sol.isSameTree(p, q) == True, "Test case 4 failed"

    # Test case 5: 다른 구조
    print("test5")    
    p = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p, q) == False, "Test case 5 failed"

    print("All test cases passed.")

# 테스트 실행
test_isSameTree()