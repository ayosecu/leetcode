class Solution:
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_max_sub = nums[0]
        current_max = 0
        sum_min_sub = nums[0]
        current_min = 0
        total_sum = 0
        for num in nums:
            current_max = max(num, current_max + num)
            sum_max_sub = max(sum_max_sub, current_max)
            current_min = min(num, current_min + num)
            sum_min_sub = min(sum_min_sub, current_min)
            total_sum += num

        # Case 3 (Edge case) : All numbers are negative => Total - SumMinSub = 0, Use Kadane Algorithm
        if total_sum - sum_min_sub == 0:
            return sum_max_sub
        else:
            # Case 1 : if max subarray exists in the middle of nums => Kadane Algorithm
            # Case 2 : if max subarray exists in both (end, start) sides => TotalSum - SumMinSub
            # Choose the max value
            return max(sum_max_sub, total_sum - sum_min_sub)

    def maxSubarraySumCircularByChatGPT(self, nums: list[int]) -> int:
        # Case 1: Maximum subarray sum using Kadane's algorithm (non-circular)
        def kadane(array):
            current_sum = max_sum = array[0]
            for num in array[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        
        # Step 1: Find the maximum subarray sum without circular property
        max_kadane = kadane(nums)

        # Step 2: Find the total sum of the array
        total_sum = sum(nums)

        # Step 3: Find the minimum subarray sum using Kadane's algorithm on the inverted array
        # but we exclude the case where the whole array is the subarray
        min_subarray_sum = kadane([-num for num in nums])

        # max_wrap represents the total sum minus the minimum subarray sum
        max_wrap = total_sum + min_subarray_sum  # equivalent to total_sum - (-min_subarray_sum)

        # Step 4: Return the maximum of the non-circular and circular cases
        # If all numbers are negative, max_wrap == total_sum, and in that case, we return max_kadane
        if max_wrap == 0:
            return max_kadane
        return max(max_kadane, max_wrap)

def run_tests():
    solution = Solution()

    # Test case 1: 원형 배열을 고려할 필요가 없는 경우 (단순 최대 부분 배열)
    nums1 = [1, -2, 3, -2]
    expected1 = 3  # 최대 부분 배열은 [3]
    result1 = solution.maxSubarraySumCircular(nums1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 원형 배열을 고려해야 하는 경우
    nums2 = [5, -3, 5]
    expected2 = 10  # 원형 배열을 고려한 최대 부분 배열은 [5, 5]
    result2 = solution.maxSubarraySumCircular(nums2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 모든 값이 음수인 경우
    nums3 = [-3, -2, -3]
    expected3 = -2  # 최대 부분 배열은 [-2]
    result3 = solution.maxSubarraySumCircular(nums3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 원형 배열을 고려할 필요가 없는 큰 양수 배열
    nums4 = [3, -1, 2, -1]
    expected4 = 4  # 최대 부분 배열은 [3, -1, 2]
    result4 = solution.maxSubarraySumCircular(nums4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 전체 배열이 원형 배열을 사용해야 할 때
    nums5 = [3, -2, 2, -3]
    expected5 = 3  # 최대 부분 배열은 [3]
    result5 = solution.maxSubarraySumCircular(nums5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6: 양수만 있는 배열
    nums6 = [5, 5, 5, 5]
    expected6 = 20  # 최대 부분 배열은 전체 배열 [5, 5, 5, 5]
    result6 = solution.maxSubarraySumCircular(nums6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()