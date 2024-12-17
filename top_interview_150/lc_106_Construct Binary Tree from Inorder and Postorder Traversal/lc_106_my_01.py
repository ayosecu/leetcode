# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        dic = {val: i for i, val in enumerate(inorder)}

        def makeTree(left, right):
            if left > right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            root_index = dic[root_val]

            root.right = makeTree(root_index + 1, right)
            root.left = makeTree(left, root_index - 1)

            return root
        
        return makeTree(0, len(inorder) - 1)


def tree_to_list(root):
    """Helper function to convert a binary tree to a list (level-order traversal)."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),  # General case
        ([2, 1, 3], [2, 3, 1], [1, 2, 3]),                                     # Small balanced tree
        ([1], [1], [1]),                                                      # Single node
        ([], [], []),                                                        # Empty tree
        ([2, 1], [2, 1], [1, 2]),                                            # Left-heavy tree
        ([1, 2], [2, 1], [1, None, 2]),                                      # Right-heavy tree
    ]

    for i, (inorder, postorder, expected) in enumerate(test_cases, 1):
        root = solution.buildTree(inorder, postorder)
        result = tree_to_list(root)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()