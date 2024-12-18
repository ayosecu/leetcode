from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        dq = deque([root])

        while dq:
            n = len(dq)
            for i in range(n):
                pop_node = dq.popleft()
                if i < n - 1:
                    pop_node.next = dq[0]
                
                if pop_node.left:
                    dq.append(pop_node.left)
                if pop_node.right:
                    dq.append(pop_node.right)
        
        return root


def create_tree(values):
    """Helper function to create a binary tree from a list of values (level-order traversal)."""
    if not values:
        return None

    nodes = [None if val is None else Node(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

def tree_to_next_pointers_list(root):
    """Helper function to convert the tree's next pointers to a list of lists."""
    result = []
    level = root

    while level:
        current = level
        level_result = []
        next_level = None

        while current:
            level_result.append(current.val)
            if not next_level:
                next_level = current.left or current.right
            current = current.next

        result.append(level_result)
        level = next_level

    return result

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, None, 7], [[1], [2, 3], [4, 5, 7]]),  # General case
        ([], []),                                              # Empty tree
        ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]]),      # Left-skewed tree
        ([1, None, 2, None, 3], [[1], [2], [3]]),  # Right-skewed tree
    ]

    for i, (values, expected) in enumerate(test_cases, 1):
        root = create_tree(values)
        connected_root = solution.connect(root)
        result = tree_to_next_pointers_list(connected_root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()