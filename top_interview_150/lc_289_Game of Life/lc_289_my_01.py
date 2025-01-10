class Solution(object):
    def gameOfLifeByCopy(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_map = [ row[:] for row in board ]

        def count_neighbor(i, j, m, n):
            dir = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
            cnt = 0
            for dr, dc in dir:
                if 0 <= i + dr < m and 0 <= j + dc < n and board_map[i + dr][j + dc] == 1:
                    cnt += 1
            return cnt 

        for i in range(m):
            for j in range(n):               
                cnt = count_neighbor(i, j, m, n)
                if board[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 0
                else:
                    if cnt == 3:
                        board[i][j] = 1 

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def countNeighbors(i, j, m, n):
            dir = [ (-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
            count = 0
            for dr, dc in dir:
                if 0 <= i + dr < m and 0 <= j + dc < n and abs(board[i + dr][j + dc]) == 1:
                    count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                cnt = countNeighbors(i, j, m, n)

                # 1 -> 0 : -1 (for counting), 0 -> 1 : 2
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and cnt == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),  # Standard case
        (
            [[1, 1], [1, 1]],
            [[1, 1], [1, 1]],
        ),  # All live cells survive
        (
            [[1, 0], [0, 0]],
            [[0, 0], [0, 0]],
        ),  # Single live cell dies
        (
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ),  # Single live cell with no neighbors dies
        (
            [[0]],
            [[0]],
        ),  # Single dead cell
    ]

    for i, (board, expected) in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        input_board = [row[:] for row in board]  # Make a copy for testing
        solution.gameOfLife(input_board)
        print(f"  Result: {input_board}")
        print(f"  Expected: {expected}")
        print(f"  {'Passed' if input_board == expected else 'Failed'}\n")

# Run the tests
run_tests()