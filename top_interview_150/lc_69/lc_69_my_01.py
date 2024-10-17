class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        i = 0
        j = (x//2)+1

        while i < j:
            if i*i <= x and (i+1)*(i+1) > x:
                return i
            mid = (i+j)//2
            if mid*mid <= x:
                i = mid
            else:
                j = mid 

        return -1

tc = [1, 2, 4, 8, 11, 2147483647]
sol = Solution()
for t in tc:
    print(sol.mySqrt(t))