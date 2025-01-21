from typing import List
from collections import deque

class Solution:
    def generateParenthesisByRecursive(self, n: int) -> List[str]:
        if n < 1:
            return []
        
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
            
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        result = []        
        backtrack("", 0, 0)
    
        return result
    
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []        
        dq = deque([("", 0, 0)])

        while dq:
            s, left, right = dq.popleft()

            if len(s) == 2 * n:
                result.append(s)
            
            if left < n:
                dq.append((s + "(", left + 1, right))
            if right < left:
                dq.append((s + ")", left, right + 1))
        
        return result


def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        (1, ["()"]),                        # Single pair of parentheses
        (2, ["(())", "()()"]),              # Two pairs
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),  # Three pairs
        (0, []),                            # No parentheses
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.generateParenthesis(n)
        # Sort both lists to ensure order-independent comparison
        print(f"Test case {i}: {'Passed' if sorted(result) == sorted(expected) else 'Failed'}, Result: {sorted(result)}, Expected: {sorted(expected)}")

# Run the tests
run_tests()