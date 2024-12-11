class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def getSumSquares(num):
            digits = [int(digit) ** 2 for digit in str(num)]
            return sum(digits)
        
        seen_nums = set()

        while n != 1:
            n = getSumSquares(n)
            if n in seen_nums:
                return False
            seen_nums.add(n)
        
        return True

tc = [ (19, True), (2, False) ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.isHappy(t[0])
    assert result == t[1], "TC {} Failed - Expected: {}, Result: {}".format(i + 1, t[1], result)
    print(f"TC {i + 1} Passed!!")
