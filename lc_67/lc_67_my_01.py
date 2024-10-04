class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = int(a, 2) + int(b, 2)
        return "{0:b}".format(result)
    
sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))