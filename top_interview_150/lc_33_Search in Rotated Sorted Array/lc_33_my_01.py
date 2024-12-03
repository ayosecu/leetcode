class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    expected1 = 4
    result1 = solution.search(nums1, target1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    expected2 = -1
    result2 = solution.search(nums2, target2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    target3 = 5
    expected3 = 4
    result3 = solution.search(nums3, target3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    nums4 = [1]
    target4 = 1
    expected4 = 0
    result4 = solution.search(nums4, target4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    nums5 = [1]
    target5 = 0
    expected5 = -1
    result5 = solution.search(nums5, target5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    nums6 = []
    target6 = 1
    expected6 = -1
    result6 = solution.search(nums6, target6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()