# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(node, sum):
            # check leaf node
            if not node.left and not node.right:
                return node.val + sum == targetSum
            
            left_ret, right_ret = False, False
            if node.left:
                left_ret = dfs(node.left, node.val + sum)
            if node.right:
                right_ret = dfs(node.right, node.val + sum)
            return left_ret + right_ret
        
        return dfs(root, 0)


def create_binary_tree(values):
    """Helper function to create a binary tree from a list of values (level-order traversal)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),  # Example with valid path
        ([1, 2, 3], 5, False),                                             # No valid path
        ([1, 2], 1, False),                                                # Leaf nodes don't match
        ([], 0, False),                                                    # Empty tree
        ([1, 2], 3, True),                                                 # Single valid path
    ]

    for i, (tree_values, targetSum, expected) in enumerate(test_cases, 1):
        root = create_binary_tree(tree_values)
        result = solution.hasPathSum(root, targetSum)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()