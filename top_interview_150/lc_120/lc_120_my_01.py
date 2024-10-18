class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = []
        memo.append([triangle[0][0]])
    
        for i in range(0, len(triangle)-1):
            memo.append([2000001 for _ in range(i+2)])
            for j in range(len(triangle[i])):
                memo[i+1][j] = min(memo[i+1][j], memo[i][j] + triangle[i+1][j])
                memo[i+1][j+1] = min(memo[i+1][j+1], memo[i][j] + triangle[i+1][j+1])

        return min(memo[-1])
    
def run_tests():
    solution = Solution()

    # Test case 1: 삼각형에 최소 경로가 존재하는 경우
    triangle1 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    expected1 = 11  # 경로: 2 → 3 → 5 → 1
    result1 = solution.minimumTotal(triangle1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 한 줄짜리 삼각형
    triangle2 = [
        [-10]
    ]
    expected2 = -10  # 경로: -10
    result2 = solution.minimumTotal(triangle2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 모든 값이 0인 삼각형
    triangle3 = [
        [0],
        [0, 0],
        [0, 0, 0]
    ]
    expected3 = 0  # 모든 값이 0이므로 최소 경로 합도 0
    result3 = solution.minimumTotal(triangle3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 음수 값이 포함된 삼각형
    triangle4 = [
        [1],
        [2, 3],
        [1, -1, -3]
    ]
    expected4 = 1  # 경로: 1 → 3 → -3
    result4 = solution.minimumTotal(triangle4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 모든 값이 동일한 삼각형
    triangle5 = [
        [1],
        [1, 1],
        [1, 1, 1]
    ]
    expected5 = 3  # 경로: 1 → 1 → 1
    result5 = solution.minimumTotal(triangle5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()