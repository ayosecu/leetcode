import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def myMaxHeap(list):
            l = []
            for num in list:
                heapq.heappush(l, -num)
            return [ -heapq.heappop(l) for _ in range(len(l)) ]
        
        return myMaxHeap(nums)[k-1]

def run_tests():
    solution = Solution()

    # Test case 1: k번째로 큰 값이 배열 중간에 있는 경우
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = solution.findKthLargest(nums1, k1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 중복된 값이 있는 경우
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 배열의 모든 요소가 동일한 경우
    nums3 = [1, 1, 1, 1, 1]
    k3 = 1
    expected3 = 1
    result3 = solution.findKthLargest(nums3, k3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 음수가 포함된 경우
    nums4 = [-1, -2, -3, -4, -5]
    k4 = 3
    expected4 = -3
    result4 = solution.findKthLargest(nums4, k4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: k가 1일 때 (가장 큰 값 찾기)
    nums5 = [2, 3, 4, 5, 6]
    k5 = 1
    expected5 = 6
    result5 = solution.findKthLargest(nums5, k5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()