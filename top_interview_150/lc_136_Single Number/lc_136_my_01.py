class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        xor = 0
        for n in nums:
            xor ^= n
        
        return xor

tc = [
        [[2, 2, 1], 1],
        [[4, 1, 2, 1, 2], 4],
        [[1], 1]
    ]

sol = Solution()

for i in range(len(tc)):
    result = sol.singleNumber(tc[i][0])
    expected = tc[i][1]
    assert result == expected, "TC {} Failed - Expected: {}, Result: {}".format(i + 1, expected, result)
    print(f"TC {i + 1} Passed!")
