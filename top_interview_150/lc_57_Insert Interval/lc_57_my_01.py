class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        n = len(intervals)

        i = 0
        # 1. front intervals adding (intervals[i][1] less than newInterval[0])
        while i < n and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1
        
        # 2. merge interval using min/max
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ret.append(newInterval)

        # 3. remain intervals adding
        while i < n:
            ret.append(intervals[i])
            i += 1
        
        return ret

def run_tests():
    solution = Solution()

    # Test case 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    expected1 = [[1, 5], [6, 9]]
    result1 = solution.insert(intervals1, newInterval1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    expected2 = [[1, 2], [3, 10], [12, 16]]
    result2 = solution.insert(intervals2, newInterval2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    intervals3 = [[5, 7], [8, 12]]
    newInterval3 = [1, 4]
    expected3 = [[1, 4], [5, 7], [8, 12]]
    result3 = solution.insert(intervals3, newInterval3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    intervals4 = [[1, 3], [4, 6]]
    newInterval4 = [7, 9]
    expected4 = [[1, 3], [4, 6], [7, 9]]
    result4 = solution.insert(intervals4, newInterval4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    intervals5 = []
    newInterval5 = [4, 8]
    expected5 = [[4, 8]]
    result5 = solution.insert(intervals5, newInterval5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()