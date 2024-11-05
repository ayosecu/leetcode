from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False

        s_set = defaultdict(int)
        for i in range(s_len):
            s_set[s[i]] += 1
            s_set[t[i]] -= 1
          
        for v in s_set.values():
            if v != 0:
                return False

        return True

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