# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        root_idx = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx + 1:])

        return root

def tree_to_list(root: TreeNode) -> list[int]:
    """Convert a binary tree to a list using level-order traversal."""
    if not root:
        return []

    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

def run_tests():
    solution = Solution()

    # Test case 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    expected1 = [3, 9, 20, None, None, 15, 7]
    result1 = tree_to_list(solution.buildTree(preorder1, inorder1))
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    preorder2 = [1, 2, 3]
    inorder2 = [3, 2, 1]
    expected2 = [1, 2, None, 3]
    result2 = tree_to_list(solution.buildTree(preorder2, inorder2))
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    preorder3 = [1, 2, 3]
    inorder3 = [1, 2, 3]
    expected3 = [1, None, 2, None, 3]
    result3 = tree_to_list(solution.buildTree(preorder3, inorder3))
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    preorder4 = [1]
    inorder4 = [1]
    expected4 = [1]
    result4 = tree_to_list(solution.buildTree(preorder4, inorder4))
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    preorder5 = []
    inorder5 = []
    expected5 = []
    result5 = tree_to_list(solution.buildTree(preorder5, inorder5))
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()