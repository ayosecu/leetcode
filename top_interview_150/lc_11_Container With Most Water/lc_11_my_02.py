"""
 - Time Complexity: O(n)
 - Space Complexity: O(1)
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        max_amount = 0
        left, right = 0, len(height) - 1

        while left < right:
            amount = (right - left) * min(height[left], height[right])
            max_amount = max(max_amount, amount)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount

tc = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([], 0)
]

for i, (h, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.maxArea(h)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")
