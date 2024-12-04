class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones
    
def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 2, 3, 2]
    expected1 = 3
    result1 = solution.singleNumber(nums1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    nums2 = [0, 1, 0, 1, 0, 1, -1]
    expected2 = -1
    result2 = solution.singleNumber(nums2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    nums3 = [1, 2, 3, 2, 3, 2, 3]
    expected3 = 1
    result3 = solution.singleNumber(nums3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    nums4 = [42]
    expected4 = 42
    result4 = solution.singleNumber(nums4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    nums5 = [0, 0, 0, 1]
    expected5 = 1
    result5 = solution.singleNumber(nums5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()    