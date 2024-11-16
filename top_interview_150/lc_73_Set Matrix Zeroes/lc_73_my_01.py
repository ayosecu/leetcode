class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        is_first_row_zero = any(matrix[0][i] == 0 for i in range(n))
        is_first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        if is_first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

def run_tests():
    solution = Solution()

    # Test case 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    expected1 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    solution.setZeroes(matrix1)
    print(f"Test 1 {'passed' if matrix1 == expected1 else 'failed'}: Expected {expected1}, Got {matrix1}")

    # Test case 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    expected2 = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]
    solution.setZeroes(matrix2)
    print(f"Test 2 {'passed' if matrix2 == expected2 else 'failed'}: Expected {expected2}, Got {matrix2}")

    # Test case
    matrix3 = [
        [0, 0],
        [0, 0]
    ]
    expected3 = [
        [0, 0],
        [0, 0]
    ]
    solution.setZeroes(matrix3)
    print(f"Test 3 {'passed' if matrix3 == expected3 else 'failed'}: Expected {expected3}, Got {matrix3}")

    # Test case 4
    matrix4 = [[0]]
    expected4 = [[0]]
    solution.setZeroes(matrix4)
    print(f"Test 4 {'passed' if matrix4 == expected4 else 'failed'}: Expected {expected4}, Got {matrix4}")

    # Test case 5
    matrix5 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected5 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    solution.setZeroes(matrix5)
    print(f"Test 5 {'passed' if matrix5 == expected5 else 'failed'}: Expected {expected5}, Got {matrix5}")

# Run the tests
run_tests()