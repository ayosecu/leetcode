"""
 - Time Complexity: O(n)
 - Space Complexity: O(1)
 - Algorithm: Two Pointers
 - Note: Question is it okay to return empty list ([]) if there is not matched result.
 """
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum_val = numbers[left] + numbers[right]

            if sum_val == target:
                return [left + 1, right + 1]
            elif sum_val < target:
                left += 1
            else:
                right -= 1
        
        return []
    
tc = [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2])
]

for i, (nums, target, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.twoSum(nums, target)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")
