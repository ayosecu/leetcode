class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(path, combo):
            if not combo:
                result.append(path)
                return

            for i in range(len(combo)):
                backtrack(path + [combo[i]], combo[:i] + combo[i + 1:])

        backtrack([], nums)
        return result
    
tc = [
        [[1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]],
        [[0, 1], [[0, 1], [1, 0]]],
        [[1], [[1]]]
    ]

sol = Solution()

for i in range(len(tc)):
    result = sol.permute(tc[i][0])
    expected = tc[i][1]
    assert result == expected, "TC {} Failed - Expected: {}, Result: {}".format(i + 1, expected, result)
    print(f"TC {i + 1} Passed!")
