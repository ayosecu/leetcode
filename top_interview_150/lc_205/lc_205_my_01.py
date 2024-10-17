class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set = {}
        for i, c in enumerate(s):
            if c not in s_set:
                if t[i] in s_set.values():
                    return False
                s_set[c] = t[i]
            else:
                if s_set[c] != t[i]:
                    return False       
        return True

sol = Solution()
tc = [
        ["egg", "add"],
        ["foo", "bar"],
        ["paper", "title"],
        ["bbbaaaba", "aaabbbba"],
        ["badc", "baba"]
    ]

for t in tc:
    print(sol.isIsomorphic(t[0], t[1]))