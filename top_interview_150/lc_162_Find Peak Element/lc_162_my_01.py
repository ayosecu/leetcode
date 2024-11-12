class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1]
    expected1 = 2
    result1 = solution.findPeakElement(nums1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    expected2 = 4
    result2 = solution.findPeakElement(nums2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    nums3 = [5, 4, 3, 2, 1]
    expected3 = 0
    result3 = solution.findPeakElement(nums3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    nums4 = [1, 3, 2, 4, 3]
    expected4_possible = [1, 3]
    result4 = solution.findPeakElement(nums4)
    print(f"Test 4 {'passed' if result4 in expected4_possible else 'failed'}: Expected one of {expected4_possible}, Got {result4}")

    # Test case 5
    nums5 = [1]
    expected5 = 0
    result5 = solution.findPeakElement(nums5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()
        