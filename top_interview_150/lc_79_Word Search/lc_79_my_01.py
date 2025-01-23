from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, idx):
            if len(word) == idx:
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            
            # Matched Character, check visited
            tmp = board[r][c]
            board[r][c] = "#"

            check_neighbors = ( dfs(r - 1, c, idx + 1) or
                                dfs(r + 1, c, idx + 1) or
                                dfs(r, c - 1, idx + 1) or
                                dfs(r, c + 1, idx + 1) )
            
            # Restore origin character
            board[r][c] = tmp

            return check_neighbors
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True
        ),  # Word exists
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True
        ),  # Word exists in a different path
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False
        ),  # Word does not exist
        (
            [["A"]],
            "A",
            True
        ),  # Single cell, word exists
        (
            [["A"]],
            "B",
            False
        ),  # Single cell, word does not exist
        (
            [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]],
            "AAB",
            True
        ),  # Multiple paths exist
        (
            [["A", "B"], ["C", "D"]],
            "ACDB",
            True
        ),  # Word not possible due to invalid sequence
    ]

    for i, (board, word, expected) in enumerate(test_cases, 1):
        result = solution.exist(board, word)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()