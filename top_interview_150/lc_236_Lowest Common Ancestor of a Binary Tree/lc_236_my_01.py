# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right



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

def find_node(root, val):
    """Helper function to find a node with a specific value in a binary tree."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "tree": [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            "p": 5,
            "q": 1,
            "expected": 3,  # Root is the LCA
        },
        {
            "tree": [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            "p": 5,
            "q": 4,
            "expected": 5,  # p is the ancestor of q
        },
        {
            "tree": [1, 2],
            "p": 1,
            "q": 2,
            "expected": 1,  # Root is the LCA
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        root = create_tree(test_case["tree"])
        p = find_node(root, test_case["p"])
        q = find_node(root, test_case["q"])
        result = solution.lowestCommonAncestor(root, p, q)
        result_val = result.val if result else None
        print(f"Test case {i}: {'Passed' if result_val == test_case['expected'] else 'Failed'}, Result: {result_val}, Expected: {test_case['expected']}")

# Run the tests
run_tests()