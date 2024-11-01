class Solution(object):
    def referenceSolution(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return res
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) < 1:
            return []
        
        m = len(matrix)
        n = len(matrix[0])

        v_list = []
        visited = set()

        def goSpiral(i, j, dir):
            if (i, j) not in visited:
                v_list.append(matrix[i][j])
                visited.add((i, j))
                
            if dir == 1:
                if j+1 <= n-1 and (i, j+1) not in visited:
                    goSpiral(i, j+1, 1)
                elif i+1 <= m-1 and (i+1, j) not in visited:
                    goSpiral(i, j, 2)
            elif dir == 2:
                if i+1 <= m-1 and (i+1, j) not in visited:
                    goSpiral(i+1, j, 2)
                elif j-1 >=0 and (i, j-1) not in visited:
                    goSpiral(i, j, 3) 
            elif dir == 3:
                if j-1 >= 0 and (i, j-1) not in visited:
                    goSpiral(i, j-1, 3)
                elif i-1 >= 0 and (i-1, j) not in visited:
                    goSpiral(i, j, 4)
            elif dir == 4:
                if i-1 >= 0 and (i-1, j) not in visited:
                    goSpiral(i-1, j, 4)
                elif j+1 <= n-1 and (i, j+1) not in visited:
                    goSpiral(i, j, 1)
            return 

        goSpiral(0, 0, 1)

        return v_list

def run_tests():
    solution = Solution()

    # Test case 1: 3x3
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    result1 = solution.spiralOrder(matrix1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 3x4
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    expected2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    result2 = solution.spiralOrder(matrix2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 1x4
    matrix3 = [
        [1, 2, 3, 4]
    ]
    expected3 = [1, 2, 3, 4]
    result3 = solution.spiralOrder(matrix3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 4x1
    matrix4 = [
        [1],
        [2],
        [3],
        [4]
    ]
    expected4 = [1, 2, 3, 4]
    result4 = solution.spiralOrder(matrix4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: empty
    matrix5 = []
    expected5 = []
    result5 = solution.spiralOrder(matrix5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()