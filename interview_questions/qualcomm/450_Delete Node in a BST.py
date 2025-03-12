from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSuccessor(self, root):
        while root.left:
            root = root.left
        return root

    """
        - Time Complexity: O(H), H = Height of tree
        - Space Complexity: O(H), H = Height of tree
        - If skewed tree => H = N, N = The number of nodes
        - If balanced tree => H = logN, N = The number of nodes
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # found node with key            
            # if leaf node => return None => make child as None
            if not root.left and not root.right:
                return None            
            # if has only left node => return left node 
            if not root.right:
                return root.left
            # if has only right node => return right node
            if not root.left:
                return root.right
            
            # if has two chidren => find successor (right & most left node) => swap val => deleteNode with successor's val from right child
            successor = self.findSuccessor(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root


# Function to insert a value into a BST (used to construct test cases)
def insert_into_bst(root, val):
    if val is None:
        return root
    
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Function to create a BST from a list of values
def create_bst(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root

# Function to perform an inorder traversal (used for checking BST validity)
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# Function to print the BST inorder (for debugging)
def print_bst(root):
    print("BST Inorder:", inorder_traversal(root))

def run_tests():
    solution = Solution()

    test_cases = [
        ([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7]),  # Case 1: Delete node with two children
        ([5, 3, 6, 2, 4, None, 7], 0, [2, 3, 4, 5, 6, 7]),  # Case 2: Delete node not in tree (no change)
        ([5], 5, []),  # Case 3: Delete the only node in tree
        ([5, 3, 6, 2, None, None, 7], 6, [2, 3, 5, 7]),  # Case 4: Delete node with only right child
        ([5, 3, 6, None, 4, None, 7], 3, [4, 5, 6, 7]),  # Case 5: Delete node with only left child
        ([5, 3, 6, 2, 4, None, 7], 7, [2, 3, 4, 5, 6]),  # Case 6: Delete leaf node
    ]

    for i, (values, key, expected) in enumerate(test_cases, 1):
        root = create_bst(values)
        print(f"Test case {i}: Deleting {key}")
        root = solution.deleteNode(root, key)
        result = inorder_traversal(root)
        print(f"  Input: {values}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'Passed' if result == expected else 'Failed'}\n")

# Run the tests
run_tests()