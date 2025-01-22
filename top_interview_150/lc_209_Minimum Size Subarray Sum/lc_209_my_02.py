# Time Complexity: O(n) + O(n) => O(n)
# Space Complexity: O(1)
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")

        sum_nums, left = 0, 0
        for i in range(len(nums)):
            sum_nums += nums[i]

            while sum_nums >= target:
                min_len = min(min_len, i - left + 1)
                sum_nums -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0

tc = [
        ([2,3,1,2,4,3], 7, 2),
        ([1,4,4], 4, 1),
        ([1,1,1,1,1,1,1,1], 11, 0)
]

for i, (nums, target, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")