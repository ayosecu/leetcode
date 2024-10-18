class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for i in range(1, n):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])

        return max(nums)

sol = Solution()
tc = [ [-2,1,-3,4,-1,2,1,-5,4],[1],[5,4,-1,7,8] ]
for t in tc:
    print(sol.maxSubArray(t))
