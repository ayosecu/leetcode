class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        candy_cnt = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy_cnt[i] = candy_cnt[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_cnt[i] = max(candy_cnt[i], candy_cnt[i+1] + 1)
 
        return sum(candy_cnt)

tc = [
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
        [[2, 1, 3, 4], 8]
]

sol = Solution()
for i in range(len(tc)):
    result = sol.candy(tc[i][0])
    assert result == tc[i][1], "TC {} Failed, Expected: {}, Result: {}".format(i+1, tc[i][1], result)
    print(f"TC {i+1} Passed!")

