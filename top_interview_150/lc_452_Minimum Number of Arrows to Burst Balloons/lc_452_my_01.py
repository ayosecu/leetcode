class Solution(object):
    def findMinArrowShotsMy(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n < 1:
            return 0

        points.sort()

        base = points[0]
        i, cnt = 1, 1
        while i < n:
            if base[0] <= points[i][0] <= base[1]:
                base[0] = max(base[0], points[i][0])
                base[1] = min(base[1], points[i][1])
            else:
                cnt += 1
                base = points[i]
            i += 1
        
        return cnt

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        cnt = 1

        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                cnt += 1
                prev_end = end
        
        return cnt

def run_tests():
    solution = Solution()

    # Test case 1
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected1 = 2
    result1 = solution.findMinArrowShots(points1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected2 = 4
    result2 = solution.findMinArrowShots(points2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    points3 = [[1, 10], [2, 9], [3, 8], [4, 7]]
    expected3 = 1
    result3 = solution.findMinArrowShots(points3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    points4 = []
    expected4 = 0
    result4 = solution.findMinArrowShots(points4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    points5 = [[1, 2]]
    expected5 = 1
    result5 = solution.findMinArrowShots(points5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    points6 = [[1, 3], [2, 4], [5, 6], [7, 8]]
    expected6 = 3
    result6 = solution.findMinArrowShots(points6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()