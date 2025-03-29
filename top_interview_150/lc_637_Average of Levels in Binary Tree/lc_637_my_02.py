from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes.
        - Space Complexity: O(n)
            - dq size : n/2 => O(n/2) => O(n)
            - result size : skewed tree = O(n), balanced = O(logn)
            - dq + result : O(n) 
    """
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        dq = deque([root])
        result = []

        while dq:
            total = 0
            n = len(dq)
            for _ in range(n):
                pop_node = dq.popleft()
                total += pop_node.val

                if pop_node.left:
                    dq.append(pop_node.left)
                if pop_node.right:
                    dq.append(pop_node.right)

            result.append(total / n)
        
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

tc = [
        ([3, 9, 20, None, None, 15, 7], [3.0, 14.5, 11.0]),
        ([1, 2, 3], [1.0, 2.5]),
        ([5], [5.0]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [1.0, 2.5, 5.5])
    ]            

for i, (t, expected) in enumerate(tc, 1):
    sol = Solution()
    root1 = insert_level_order(t, None, 0, len(t))
    result = sol.averageOfLevels(root1)
    print(f"TC {i} is Passed!" if result == expected else f"TC {i} is Failed!")