class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n //= 2
        return cnt

tc = [11, 128, 2147483645, 2**31-1]
sol = Solution()
for t in tc:
    print(sol.hammingWeight(t))