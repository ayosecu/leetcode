class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[n]]
        
        result = []
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return

            for i in range(start, n+1):
                combination.append(i)
                backtrack(i+1, combination)
                combination.pop()
        
        backtrack(1, [])
        return result

sol = Solution()

tc = [
        [4, 2],
        [4, 3],
        [1, 1]
    ]
for t in tc:
    print(sol.combine(t[0], t[1]))
