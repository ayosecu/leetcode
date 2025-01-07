# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.st = []
        self.pushLeftChilds(root)
    
    def next(self):
        """
        :rtype: int
        """
        pop_node = self.st.pop()
        self.pushLeftChilds(pop_node.right)

        return pop_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0

    def pushLeftChilds(self, node):
        while node:
            self.st.append(node)
            node = node.left        


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
        ([7, 3, 15, None, None, 9, 20], [3, 7, 9, 15, 20]),  # General case
        ([], []),                                            # Empty tree
        ([1], [1]),                                         # Single node
        ([2, 1], [1, 2]),                                   # Left-skewed tree
        ([2, None, 3], [2, 3]),                             # Right-skewed tree
    ]

    for i, (values, expected) in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        root = create_tree(values)
        iterator = BSTIterator(root)

        result = []
        while iterator.hasNext():
            result.append(iterator.next())

        print(f"  Result: {result}, Expected: {expected}")
        print(f"  {'Passed' if result == expected else 'Failed'}")

# Run the tests
run_tests()