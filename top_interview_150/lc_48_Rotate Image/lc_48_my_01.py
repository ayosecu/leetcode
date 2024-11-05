class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
        
        return matrix

def run_tests():
    solution = Solution()

    # Test case 1: 3x3
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected1 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    solution.rotate(matrix1)
    print(f"Test 1 {'passed' if matrix1 == expected1 else 'failed'}: Expected {expected1}, Got {matrix1}")

    # Test case 2: 4x4
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    expected2 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    solution.rotate(matrix2)
    print(f"Test 2 {'passed' if matrix2 == expected2 else 'failed'}: Expected {expected2}, Got {matrix2}")

    # Test case 3: 1x1
    matrix3 = [
        [1]
    ]
    expected3 = [
        [1]
    ]
    solution.rotate(matrix3)
    print(f"Test 3 {'passed' if matrix3 == expected3 else 'failed'}: Expected {expected3}, Got {matrix3}")

    # Test case 4: 2x2
    matrix4 = [
        [1, 2],
        [3, 4]
    ]
    expected4 = [
        [3, 1],
        [4, 2]
    ]
    solution.rotate(matrix4)
    print(f"Test 4 {'passed' if matrix4 == expected4 else 'failed'}: Expected {expected4}, Got {matrix4}")

    # Test case 5: 5x5
    matrix5 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    expected5 = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]
    solution.rotate(matrix5)
    print(f"Test 5 {'passed' if matrix5 == expected5 else 'failed'}: Expected {expected5}, Got {matrix5}")

# Run the tests
run_tests()