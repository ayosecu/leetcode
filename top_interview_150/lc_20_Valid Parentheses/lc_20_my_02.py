class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n), n = len(s)
    """
    def isValid(self, s: str) -> bool:
        open_set = { "(", "{", "[" }
        st = []

        for c in s:
            if c in open_set:
                st.append(c)
            else:
                if not st:
                    return False
                
                pop_c = st.pop()
                if c == ")" and pop_c != "(":
                    return False
                if c == "}" and pop_c != "{":
                    return False
                if c == "]" and pop_c != "[":
                    return False

        return len(st) == 0

tc = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("[", False),
        ("]", False)
]

for i, (s, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.isValid(s)
    print(f"TC {i} is Passed!" if result == expected else f"TC {i} is Failed! - Expected: {expected}, Result: {result}")
