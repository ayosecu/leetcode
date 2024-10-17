# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def __init__(self):
        self.min_diff = 100000
        self.prev_val = None

    def in_order(self, node):
        if node is None:
            return
        
        self.in_order(node.left)

        if self.prev_val is not None:
            self.min_diff = min(abs(self.prev_val - node.val), self.min_diff)
        self.prev_val = node.val

        self.in_order(node.right)
        return

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.in_order(root)        
        return self.min_diff
    
# 테스트 케이스 실행 함수
def run_test():
    # 테스트 케이스 1: [4, 2, 6, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 1 - Expected: 1, Result:", result)

    # 테스트 케이스 2: [1, 0, 48, None, None, 12, 49]    
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(48)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(49)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 2 - Expected: 1, Result:", result)

    # 테스트 케이스 3: [236, 104, 701, None, 227, None, 911]
    root = TreeNode(236)
    root.left = TreeNode(104)
    root.right = TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)
    
    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Test Case 3 - Expected: 9, Result:", result)

# 테스트 케이스 실행
run_test()