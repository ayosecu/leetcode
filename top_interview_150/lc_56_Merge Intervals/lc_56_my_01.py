class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """     
        result = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

def run_tests():
    solution = Solution()

    # Test case 1: Simple Overlap
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected1 = [[1, 6], [8, 10], [15, 18]]
    result1 = solution.merge(intervals1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: All Overlap
    intervals2 = [[1, 4], [2, 3], [3, 6]]
    expected2 = [[1, 6]]
    result2 = solution.merge(intervals2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: No Overlap
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    expected3 = [[1, 2], [3, 4], [5, 6]]
    result3 = solution.merge(intervals3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: One Overlap
    intervals4 = [[1, 4], [4, 5]]
    expected4 = [[1, 5]]
    result4 = solution.merge(intervals4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: ALl Same
    intervals5 = [[2, 3], [2, 3], [2, 3]]
    expected5 = [[2, 3]]
    result5 = solution.merge(intervals5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()