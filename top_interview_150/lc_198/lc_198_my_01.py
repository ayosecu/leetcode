class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        memo = [0] * n
        for i in range(2):
            memo[i] = nums[i]
        for i in range(2, n):
            memo[i] = max(memo[:i-1]) + nums[i]
        
        return max(memo[-2], memo[-1])

tc = [
        [1,2,3,1],
        [2,7,9,3,1]
    ]
sol = Solution()
for t in tc:
    print(sol.rob(t))