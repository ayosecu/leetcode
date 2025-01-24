"""
    - Time Complexity: O(n), n = len(nums)
    - Space Complexity: O(1)
    - Note
        - Using writer pointer
        - Increase writer pointer just before update value.
        _ Writer pointer is the last index of unique items, so return +1 for the length.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Remove all duplicated numbers from the nums list
        # return the number of unique items
        if not nums:
            return 0
        
        # writer pointer
        w_ptr, i = 0, 1
        while i < len(nums):
            if nums[w_ptr] != nums[i]:
                w_ptr += 1 
                nums[w_ptr] = nums[i]
            i += 1
       
        return w_ptr + 1

tc = [
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),
        ([1, 1, 1], 1),
        ([], 0)
    ]

for i, (nums, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed!! - Expected: {expected}, Result: {result}")

            