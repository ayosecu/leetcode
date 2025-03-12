class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n), n = len(s) <= maximum stack size
    """
    def minAddToMakeValidStack(self, s: str) -> int:
        st = []
        for c in s:
            if c == "(":
                st.append(c)
            elif c == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    st.append(c)
        
        return len(st)

    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1), 2 counters
    """
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        close_cnt = 0

        for c in s:
            if c == "(":
                open_cnt += 1
            else:
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    close_cnt += 1
        
        return open_cnt + close_cnt

def run_tests():
    solution = Solution()

    test_cases = [
        ("())", 1),
        ("(((", 3),
        ("", 0),
        (")))((", 5),
        ("()()", 0),
        ("())(()", 2),
        ("(((((((((", 9),
        ("(()(()())())", 0),
        ("))))", 4),
        ("((()))())", 1),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.minAddToMakeValid(s)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: \"{s}\"")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()