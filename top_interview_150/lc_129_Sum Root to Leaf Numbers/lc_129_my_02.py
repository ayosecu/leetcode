from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - BFS Algorithm
        - Time Complexity: O(n), n = len(Nodes)
        - Space Complexity: O(n), n = len(Nodes)
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dq = deque([(root, root.val)])
        total = 0
        
        while dq:
            node, sum_vals = dq.popleft()

            if not node.left and not node.right:
                total += sum_vals

            if node.left:
                dq.append((node.left, sum_vals * 10 + node.left.val))
            if node.right:
                dq.append((node.right, sum_vals * 10 + node.right.val))
        
        return total

    """
        - DFS Algorithm
        - Time Complexity: O(n), n = len(nodes)
        - Space Complexity:
            - Balanced Tree - O(logn), n = len(nodes)
            - Skewed Tree O(n), n = len(nodes)
    """
    def sumNumbersDFS(self, root: Optional[TreeNode]) -> int:

        def dfs(node, sumVals):
            if not node:
                return 0
            
            sumVals = sumVals * 10 + node.val

            if not node.left and not node.right:
                return sumVals
            
            return dfs(node.left, sumVals) + dfs(node.right, sumVals)
        
        return dfs(root, 0)


def create_tree(values):
    """Helper function to create a binary tree from a list of values (level-order traversal)."""
    if not values:
        return None

    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

def run_tests():
    # Test cases
    test_cases = [
        ([1, 2, 3], 25),                      # Tree: [1, 2, 3], Paths: 12, 13
        ([4, 9, 0, 5, 1], 1026),              # Tree: [4, 9, 0, 5, 1], Paths: 495, 491, 40
        ([], 0),                              # Empty tree
        ([1], 1),                             # Single node
        ([1, 2], 12),                         # Left-skewed tree
        ([1, None, 3], 13),                   # Right-skewed tree
    ]

    for i, (values, expected) in enumerate(test_cases, 1):
        solution = Solution()
        root = create_tree(values)
        result = solution.sumNumbers(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()