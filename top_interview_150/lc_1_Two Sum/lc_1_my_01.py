from collections import defaultdict

class Solution(object):
    def twoSum_nLog(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, n - 1
        dic = defaultdict(list)

        for i in range(n):
            dic[nums[i]].append(i)

        nums.sort()
        while left < right:
            sum_val = nums[left] + nums[right]
            if sum_val == target:
                return [ dic[nums[left]].pop(), dic[nums[right]].pop() ]
            elif sum_val < target:
                left += 1
            else:
                right -= 1
        
        return []

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dic = {}

        for i in range(n):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            dic[nums[i]] = i
        
        return []

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]  # 2 + 7 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    nums2 = [-3, 4, 3, 90]
    target2 = 0
    expected2 = [0, 2]  # -3 + 3 = 0
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]  # 3 + 3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    target4 = 6
    expected4 = [1, 3]  # 2 + 4 = 6
    result4 = solution.twoSum(nums4, target4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    nums5 = [1, 2, 3]
    target5 = 7
    expected5 = []
    result5 = solution.twoSum(nums5, target5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()