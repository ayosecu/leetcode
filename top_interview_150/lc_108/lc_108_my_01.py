# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = len(nums) // 2
        node = TreeNode()
        node.val = nums[mid]
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

# Helper function to print the tree in pre-order traversal for testing purposes
def preOrder(node):
    if not node:
        return []
    return [node.val] + preOrder(node.left) + preOrder(node.right)

from collections import deque
def bfs(node):
    q = deque([node])
    result = []
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result

# Test the sortedArrayToBST function
def test_sortedArrayToBST():
    solution = Solution()
    
    # Test case 1
    nums = [-10, -3, 0, 5, 9]
    tree = solution.sortedArrayToBST(nums)
    #print("Pre-order traversal of the tree:", preOrder(tree))
    print("BFS traversal of the tree:", bfs(tree))

    # Test case 2
    nums = [1, 2, 3, 4, 5, 6, 7]
    tree = solution.sortedArrayToBST(nums)
    #print("Pre-order traversal of the tree:", preOrder(tree))
    print("BFS traversal of the tree:", bfs(tree))

    # Test case 3
    nums = [0, 1]
    tree = solution.sortedArrayToBST(nums)
    #print("Pre-order traversal of the tree:", preOrder(tree))
    print("BFS traversal of the tree:", bfs(tree))

# Run the test
test_sortedArrayToBST()        