class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(combi, start):
            result.append(list(combi))

            for i in range(start, len(nums)):
                combi.append(nums[i])
                backtrack(combi, i + 1)
                combi.pop()

        backtrack([], 0)
        return result

tc = [
        [1, 2, 3],
        [0]
    ]

sol = Solution()
for t in tc:
    print(sol.subsets(t))