# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        pre_list, post_list = [], []
        
        def preOrder(node, level):
            if not node:
                pre_list.append((None, level))    
                return
            preOrder(node.left, level+1)
            pre_list.append((node.val, level))
            preOrder(node.right, level+1)
        
        def postOrder(node, level):
            if not node:
                post_list.append((None, level))
                return
            postOrder(node.right, level+1)
            post_list.append((node.val, level))
            postOrder(node.left, level+1)
        
        preOrder(root.left, 1)
        postOrder(root.right, 1)

        if len(pre_list) != len(post_list):
            return False
        
        for i in range(len(pre_list)):
            if pre_list[i] != post_list[i]:
                return False
        
        return True

def run_tests():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    expected1 = True
    result1 = solution.isSymmetric(root1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    expected2 = False
    result2 = solution.isSymmetric(root2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    root3 = None

    expected3 = True
    result3 = solution.isSymmetric(root3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    root4 = TreeNode(1)

    expected4 = True
    result4 = solution.isSymmetric(root4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)

    expected5 = False
    result5 = solution.isSymmetric(root5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()