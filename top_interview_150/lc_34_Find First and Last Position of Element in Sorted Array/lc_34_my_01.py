class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(isLeft):
            n = len(nums)
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if isLeft:
                        if mid == left or nums[mid - 1] != target:
                            return mid
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] != target:
                            return mid
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        start = binSearch(True)
        if start == -1:
            return [-1, -1]
        end = binSearch(False)

        return [start, end]

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),    # Target is in the middle
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),  # Target not found
        ([1], 1, [0, 0]),                    # Single element matching
        ([1], 0, [-1, -1]),                  # Single element not matching
        ([], 0, [-1, -1]),                   # Empty array
        ([2, 2, 2, 2], 2, [0, 3]),          # All elements are the target
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.searchRange(nums, target)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()