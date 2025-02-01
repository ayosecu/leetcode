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
        - Time Complexity: O(n), n = len(root)
        - Space Complexity: O(n), n = len(root)
        - Note
            - Add only the last nodes in each levels to the result list.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        dq = deque([root])

        while dq:
            dq_len = len(dq)

            pop_node = None
            for _ in range(dq_len):
                pop_node = dq.popleft()
                
                if pop_node.left:
                    dq.append(pop_node.left)
                if pop_node.right:
                    dq.append(pop_node.right)
            
            result.append(pop_node.val)

        return result

    
def doTest():
    sol = Solution()
    test1 = TreeNode(1)
    test1.left = TreeNode(2)
    test1.right = TreeNode(3)
    test1.left.right = TreeNode(5)
    test1.right.right = TreeNode(4)
    result1 = sol.rightSideView(test1)
    expected1 = [1, 3, 4]
    print(f"TC 1 Passed!" if expected1 == result1 else f"TC 1 Failed!! - Expected: {expected1}, Result:{result1}")

    test2 = TreeNode(1)
    test2.right = TreeNode(3)
    result2 = sol.rightSideView(test2)
    expected2 = [1, 3]
    print(f"TC 2 Passed!" if expected2 == result2 else f"TC 2 Failed!! - Expected: {expected2}, Result:{result2}")

    test3 = TreeNode(1)
    test3.left = TreeNode(2)
    result3 = sol.rightSideView(test3)
    expected3 = [1, 2]
    print(f"TC 3 Passed!" if expected3 == result3 else f"TC 3 Failed!! - Expected: {expected3}, Result:{result3}")

doTest()