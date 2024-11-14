class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 >= 0 and j - 1 >= 0:
                    grid[i][j] = min(grid[i][j] + grid[i - 1][j], grid[i][j] + grid[i][j - 1])
                elif i - 1 >= 0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                elif j - 1 >= 0:
                    grid[i][j] = grid[i][j] + grid[i][j - 1]

        return grid[-1][-1]                    

def run_tests():
    solution = Solution()

    # Test case 1
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    expected1 = 7
    result1 = solution.minPathSum(grid1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    grid2 = [
        [1, 2],
        [1, 1]
    ]
    expected2 = 3
    result2 = solution.minPathSum(grid2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    grid3 = [[5]]
    expected3 = 5
    result3 = solution.minPathSum(grid3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    grid4 = [[1, 2, 3]]
    expected4 = 6
    result4 = solution.minPathSum(grid4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    grid5 = [[1], [2], [3]]
    expected5 = 6
    result5 = solution.minPathSum(grid5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()