from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        
        queue = deque() # Deque is more faster than normal queue
        result = []

        queue.append(root)
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val              
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(float(level_sum/level_count))
        
        return result
    
# Helper function to create a binary tree from a list of values (similar to the previous code)
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp

        if root is not None:
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

sol = Solution()
# Test case 1
arr1 = [3, 9, 20, None, None, 15, 7]
root1 = insert_level_order(arr1, None, 0, len(arr1))
print("Test Case 1 - Expected Output: [3.0, 14.5, 11.0]")
print("Output:", sol.averageOfLevels(root1))

# Test case 2
arr2 = [1, 2, 3]
root2 = insert_level_order(arr2, None, 0, len(arr2))
print("\nTest Case 2 - Expected Output: [1.0, 2.5]")
print("Output:", sol.averageOfLevels(root2))

# Test case 3 (single node)
arr3 = [5]
root3 = insert_level_order(arr3, None, 0, len(arr3))
print("\nTest Case 3 - Expected Output: [5.0]")
print("Output:", sol.averageOfLevels(root3))

# Test case 4 (empty tree)
arr4 = []
root4 = insert_level_order(arr4, None, 0, len(arr4))
print("\nTest Case 4 - Expected Output: []")
print("Output:", sol.averageOfLevels(root4))

# Test case 5 (complete tree)
arr5 = [1, 2, 3, 4, 5, 6, 7]
root5 = insert_level_order(arr5, None, 0, len(arr5))
print("\nTest Case 5 - Expected Output: [1.0, 2.5, 5.5]")
print("Output:", sol.averageOfLevels(root5))