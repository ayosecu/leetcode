"""
    - Time Complexity: O(n), n = len(nums)
    - Space Complexity: O(1)
    - Note
        - Using writer pointer, values can be updated in place.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove value from nums list
        # no order required, return the count of remains items

        # writer pointer
        w_ptr, i = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[w_ptr] = nums[i]
                w_ptr += 1
            i += 1

        return w_ptr

tc = [
        ([3, 2, 2, 3], 3, 2),
        ([0,1,2,2,3,0,4,2], 2, 5)
    ]

for i, (nums, val, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.removeElement(nums, val)
    print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed - Expected: {expected}, Result: {result}")
