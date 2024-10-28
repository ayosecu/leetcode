from typing import List

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) < 1:
            return

        m = len(board)
        n = len(board[0])

        def dfs(row, col):
            if row < 0 or row > m - 1 or col < 0 or col > n - 1 or board[row][col] != "O":
                return
            board[row][col] = "#"
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)
        
        # visiting edge connected region and change "O" -> "#"
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        
        # change "O" (island region) -> "X" and "#" (edge connected region) -> "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        return board

# 테스트 코드
def print_board(board: List[List[str]]):
    for row in board:
        print("".join(row))

if __name__ == "__main__":
    solution = Solution()
    
    # 테스트 케이스 1
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board1)
    print("Test Case 1:")
    print_board(board1)
    # Expected output:
    # XXXX
    # XXXX
    # XXXX
    # XOXX
    
    # 테스트 케이스 2
    board2 = [
        ["X", "O", "X", "X"],
        ["O", "X", "O", "X"],
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"]
    ]
    solution.solve(board2)
    print("\nTest Case 2:")
    print_board(board2)
    # Expected output:
    # XOXO
    # OXXO
    # XOXO
    # OXXO

    # 테스트 케이스 3
    board3 = [
        ["X"]
    ]
    solution.solve(board3)
    print("\nTest Case 3:")
    print_board(board3)
    # Expected output:
    # X

    # 테스트 케이스 4
    board4 = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ]
    solution.solve(board4)
    print("\nTest Case 4:")
    print_board(board4)
    # Expected output:
    # OOO
    # OOO
    # OOO