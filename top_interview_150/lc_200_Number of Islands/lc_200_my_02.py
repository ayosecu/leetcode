from typing import List

class Solution:
    """
        - Time Complexity: O(m x n)
        - Space Complexity: O(m x n)
        - Note
            - Stack uses memory and dfs recursive calling uses maximum m x n space. (all "1" in the matrix)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r, c - 1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count


tc = [
    ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1),
    ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
    ([["1","1","1"],["0","1","0"],["1","1","1"]], 1)
    ]

for i, (t, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.numIslands(t)
    print(f"Test {i} Passed!!" if result == expected else f"Test {i} Failed!! - Expected: {expected}, Result: {result}")