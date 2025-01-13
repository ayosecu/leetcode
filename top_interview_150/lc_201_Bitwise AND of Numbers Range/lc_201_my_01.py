class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift_cnt = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift_cnt += 1
        
        return left << shift_cnt


tc = [
        (5, 7, 4),
        (0, 0, 0),
        (1, 2147483647, 0)
    ]

for i, (left, right, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.rangeBitwiseAnd(left, right)
    assert result == expected, "TC {} Failed! - Expected: {} != Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")
