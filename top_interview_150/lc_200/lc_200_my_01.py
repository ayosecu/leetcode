class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """      
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return           
            grid[i][j] = "0"    # visited
            dfs(i-1, j) # up
            dfs(i, j-1) # left
            dfs(i, j+1) # right
            dfs(i+1, j) # down

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt


tc = [
    [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
    [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],
    [["1","1","1"],["0","1","0"],["1","1","1"]]
    ]

sol = Solution()
for t in tc:
    print(sol.numIslands(t))