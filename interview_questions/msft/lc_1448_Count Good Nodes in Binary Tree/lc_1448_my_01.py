# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 0
            new_max = max_val

            if node.val >= max_val:
                new_max = node.val
                count += 1
            
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, float("-inf"))
    
# Helper function to build a tree from list input
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

# Test cases
def run_tests():
    solution = Solution()

    test_cases = [
        # Format: (tree as list, expected result)
        ([3, 1, 4, 3, None, 1, 5], 4),  # Example 1
        ([3, 3, None, 4, 2], 3),  # Example 2
        ([1], 1),  # Single node case
        ([2, 4, 10, 8, None, None, 9], 4),  # Tree with increasing left side
        ([10, 5, 15, 1, 7, 12, 18], 3),  # Fully populated tree
        ([3, 3, 3, 3, 3, 3, 3], 7),  # All nodes have the same value
        ([10, 5, 1, None, 7, None, None, None, 8], 1),  # Mixed tree with some decreasing values
    ]

    for i, (tree_list, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        result = solution.goodNodes(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input Tree: {tree_list}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()