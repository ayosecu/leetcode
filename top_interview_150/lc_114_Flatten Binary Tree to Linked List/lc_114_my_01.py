# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


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

def tree_to_list(root):
    """Helper function to convert a flattened tree to a list."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

def run_tests():

    # Test cases
    test_cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),  # General case
        ([], []),                                        # Empty tree
        ([1], [1]),                                     # Single node
        ([1, 2], [1, 2]),                               # Left-skewed tree
        ([1, None, 2], [1, 2]),                         # Right-skewed tree
    ]

    for i, (values, expected) in enumerate(test_cases, 1):
        solution = Solution()
        root = create_tree(values)        
        solution.flatten(root)
        result = tree_to_list(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()