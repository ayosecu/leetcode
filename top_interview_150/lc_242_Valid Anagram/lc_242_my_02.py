from collections import Counter

class Solution:
    """
        - Time Complexity: O(n + m), n = len(s), m = len(t)
        - Space Complexity: O(N + M),
            - N = The number of unique characters in s, M = The number of unique characters in t.
            - if s and t is consist of lowercase English(26), it would be O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

tc = [
        ["anagram", "nagaram", True],
        ["rat", "car", False],
        ["aacc", "ccac", False]
    ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.isAnagram(t[0], t[1])
    assert result == t[2], "TC {} Failed - Expected: {}, Result: {}".format(i+1, t[2], result)
    print(f"TC {i+1} Passed!")