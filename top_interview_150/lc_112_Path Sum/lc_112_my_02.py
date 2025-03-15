from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(N), N = The number of nodes
        - Space Complexity: O(H), H = The height of tree
            - Skewed Tree: H = N
            - Balanced Tree: H = logN
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            # leaf node
            if root.val == targetSum:
                return True
            else:
                return False

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

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