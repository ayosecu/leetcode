class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        return [1] + digits

tc = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
        [9,9,9,9,9,9,9,9]
    ]

sol = Solution()
for t in tc:
    print(sol.plusOne(t))