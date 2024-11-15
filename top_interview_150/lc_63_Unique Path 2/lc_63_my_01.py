class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
            
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
        
        return obstacleGrid[-1][-1]
                

def run_tests():
    solution = Solution()

    # Test case 1
    grid1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected1 = 6
    result1 = solution.uniquePathsWithObstacles(grid1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    grid2 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected2 = 2
    result2 = solution.uniquePathsWithObstacles(grid2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    grid3 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected3 = 0
    result3 = solution.uniquePathsWithObstacles(grid3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    grid4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    expected4 = 0 
    result4 = solution.uniquePathsWithObstacles(grid4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    grid5 = [[0, 0, 1]]
    expected5 = 0
    result5 = solution.uniquePathsWithObstacles(grid5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    grid6 = [
        [0],
        [1],
        [0]
    ]
    expected6 = 0
    result6 = solution.uniquePathsWithObstacles(grid6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()
