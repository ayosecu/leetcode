class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//n][mid%n] == target:
                return True
            if target > matrix[mid//n][mid%n]: ## right side
                left = mid + 1
                continue
            if target < matrix[mid//n][mid%n]:  ## left side
                right = mid - 1      

        return False

tc = [
        [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3],
        [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13]
    ]
expects = [ True, False ]

sol = Solution()
for i in range(len(tc)):
    result = sol.searchMatrix(tc[i][0], tc[i][1])
    assert result == expects[i], "TC {} failed: expected:{}, result:{}".format(i+1, expects[i], result)
    print(f"Test case {i+1} passed!")
