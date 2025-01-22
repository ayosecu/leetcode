"""
    - Time Complexity: O(n^2)
        - Sort algorithm has O(nlogn) and for-while loop has O(n^2).
        - O(nlogn) + O(n^2) => O(n^2)
    - Space Complexity: O(n)
        - The Python's sort (timsort) has O(n) time complexity (General sort has O(logn) space complexity)
        - O(n) + O(1) => O(n)
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # bypassing same values from each side
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


tc = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
    ]

for i, (nums, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.threeSum(nums)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")