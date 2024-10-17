class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_range = 100001

        left, sum = 0, 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_range = min(min_range, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if min_range == 100001 else min_range

def run_tests():
    solution = Solution()
    
    # Test case 1: target = 7, nums = [2,3,1,2,4,3]
    # 최소 부분 배열은 [4,3]으로 길이는 2
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    expected1 = 2
    result1 = solution.minSubArrayLen(target1, nums1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")
    
    # Test case 2: target = 15, nums = [1,2,3,4,5]
    # 최소 부분 배열은 [5]로 길이는 5
    target2 = 15
    nums2 = [1, 2, 3, 4, 5]
    expected2 = 5
    result2 = solution.minSubArrayLen(target2, nums2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: target = 4, nums = [1, 4, 4]
    # 최소 부분 배열은 [4]로 길이는 1
    target3 = 4
    nums3 = [1, 4, 4]
    expected3 = 1
    result3 = solution.minSubArrayLen(target3, nums3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: target = 11, nums = [1,1,1,1,1,1,1,1]
    # 합계를 만족하는 부분 배열이 없으므로 결과는 0
    target4 = 11
    nums4 = [1, 1, 1, 1, 1, 1, 1, 1]
    expected4 = 0
    result4 = solution.minSubArrayLen(target4, nums4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")
    
# Run the tests
run_tests()        