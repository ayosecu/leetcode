"""
 - Time Complexity: O(n), n = len(s)
 - Space Complexity: O(1)
"""
class Solution:
    def isSubsequenceFullPass(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


tc = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("abbc", "ahbdc", False),
        ("aza", "abzba", True)
]

for i, (s, t, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.isSubsequenceFullPass(s, t)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")