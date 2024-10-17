class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        
        str = []
        i = 0
        while x >= 10**i:
            num = x % (10**(i+1))
            num //= 10**(i)
            str.append(num)
            i += 1

        i -= 1
        j = 0
        while j <= i:
            if str[i] != str[j]:
                return False
            j += 1
            i -= 1

        return True


tc = [ 121, -121, 10, -11 ]
sol = Solution()
for t in tc:
    print(sol.isPalindrome(t))