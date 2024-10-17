class Solution(object):
    def myFIrstIsValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_set = set()

        # case 1 not satisfied
        for j in range(len(board[0])):
            check_set.clear()
            for i in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in check_set:
                        return False
                    check_set.add(board[i][j])

        # case 2 not satisfied
        for i in range(len(board)):
            check_set.clear()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in check_set:
                        return False
                    check_set.add(board[i][j])

        # case 3 not satisfied
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                check_set.clear()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != ".":
                            if board[i+k][j+l] in check_set:
                                return False
                            check_set.add(board[i+k][j+l])
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_check = [ set() for _ in range(9) ]
        col_check = [ set() for _ in range(9) ]
        sub_check = [ set() for _ in range(9) ]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val == ".":
                    continue

                if val in row_check[i]:
                    return False
                row_check[i].add(val)

                if val in col_check[j]:
                    return False
                col_check[j].add(val)

                sub_index = (i // 3) * 3 + (j // 3)
                if val in sub_check[sub_index]:
                    return False
                sub_check[sub_index].add(val)

        return True

sol = Solution()
tc = [
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
        [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
]

for t in tc:
    print(sol.isValidSudoku(t))