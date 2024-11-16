class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                if sum_val == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1

        return result
    
def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    result1 = solution.threeSum(nums1)
    print(f"Test 1 {'passed' if sorted(result1) == sorted(expected1) else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    nums2 = [0, 0, 0, 0]
    expected2 = [[0, 0, 0]]
    result2 = solution.threeSum(nums2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    nums3 = [1, 2, 3]
    expected3 = []
    result3 = solution.threeSum(nums3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    nums4 = [-2, 0, 1, 1, 2]
    expected4 = [[-2, 0, 2], [-2, 1, 1]]
    result4 = solution.threeSum(nums4)
    print(f"Test 4 {'passed' if sorted(result4) == sorted(expected4) else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    nums5 = []
    expected5 = []
    result5 = solution.threeSum(nums5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    nums6 = [0]
    expected6 = []
    result6 = solution.threeSum(nums6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()