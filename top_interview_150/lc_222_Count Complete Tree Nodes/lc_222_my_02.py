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
        - Time Complexity: O(n), n = The number of nodes
        - Space Compexity: O(n)
            - It depends on queue size
            - Max queue size : n/2
            - The last level of tree would filled by left => Max queue size: H - 1 level's nodes' count
            - O(n/2) => O(n)
    """
    def countNodesBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = deque([root])
        
        count = 0
        while dq:
            pop_node = dq.popleft()
            count += 1
            if pop_node.left:
                dq.append(pop_node.left)
            if pop_node.right:
                dq.append(pop_node.right)
        
        return count

    """
        - Time Complexity: O(n), n = The number of nodes
        - Space Compexity: O(H)
            - H = The height of tree
            - In case of complete binary tree : H = logn, 
    """
    def countNodesDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    """
        - Time Complexity: O(H^2)
            - H = The height of tree => logn (complete binary tree)
            - countNodes called O(H) and each function calls getHeight which takes O(H).
        - Space Compexity: O(H)
            - Recurrsive call of countNodes take O(H) space for stack.
    """    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
    
        left_h = getHeight(root.left)
        right_h = getHeight(root.right)

        if left_h == right_h:
            # left tree is complete
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # right tree is complete
            return (1 << right_h) + self.countNodes(root.left)

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
        ([1, 2, 3, 4, 5, 6], 6),  # Perfect tree except last level
        ([1], 1),                 # Single node
        ([1, 2, 3], 3),           # Complete tree with two levels
        ([], 0),                  # Empty tree
        ([1, 2, 3, 4, 5], 5),     # Left-heavy complete tree
    ]

    for i, (tree_values, expected) in enumerate(test_cases, 1):
        root = create_binary_tree(tree_values)
        result = solution.countNodes(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()    