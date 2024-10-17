from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def getVal(num):
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 0:    # even row
                return board[n - 1 - row][col]
            else:               # odd row
                return board[n - 1 - row][n - 1 - col]

        q, v = deque(), set()
        q.append((1, 0))         ## init queue, add a set (pos, count)
        v.add(1)    ## visit check

        while q:
            pos, count = q.popleft()
            if pos == n * n:
                return count

            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    break
                    
                next_val = getVal(next_pos)
                if next_val != -1:
                    next_pos = next_val

                if next_pos not in v:     
                    q.append((next_pos, count + 1))
                    v.add(next_pos)
        return -1
    
def run_tests():
    solution = Solution()
    
    # Test case 1
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    expected1 = 4
    result1 = solution.snakesAndLadders(board1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    board2 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, 2, -1]
    ]
    expected2 = 4
    result2 = solution.snakesAndLadders(board2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    board3 = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, -1, -1]
    ]
    expected3 = 1
    result3 = solution.snakesAndLadders(board3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: No solution
    board4 = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    expected4 = 2
    result4 = solution.snakesAndLadders(board4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 1
    board5 = [
        [-1, 4],
        [-1, 3]
    ]
    expected5 = 1
    result5 = solution.snakesAndLadders(board5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()