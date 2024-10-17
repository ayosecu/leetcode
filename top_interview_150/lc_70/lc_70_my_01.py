class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        memo = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                memo[i] = 1
            else:
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n-1] + memo[n-2]

sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(45))