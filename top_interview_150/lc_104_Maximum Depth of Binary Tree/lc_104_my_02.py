from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n), n = the number of nodes
    # Space Complexity: O(H), H = Height of the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS, count depth by calling dfs, and choose max depth        
        def dfs(node, depth):
            if not node:
                return depth           
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        
        return dfs(root, 0)


# Helper function to build a binary tree from a list (level-order)
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
        ([3, 9, 20, None, None, 15, 7], 3),  # Example 1
        ([1, None, 2], 2),  # Skewed tree
        ([1, 2, 3, 4, 5], 3),  # Balanced tree
        ([1], 1),  # Single node tree
        ([], 0),  # Empty tree
        ([1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5], 5),  # Left-skewed tree
        ([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5], 5),  # Right-skewed tree
        ([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9], 4),  # Complete tree
    ]

    for i, (tree_list, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        result = solution.maxDepth(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input Tree: {tree_list}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()