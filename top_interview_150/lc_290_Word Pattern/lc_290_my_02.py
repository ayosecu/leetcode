class Solution:
    """
        - Time Complexity: O(N), N = len(pattern)
        - Space Complexity: O(P + W)
            - P = The number of unique character in pattern
            - W = The number of unique word in s
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        atow_dic = {}
        wtoa_dic = {}
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False

        for c, w in zip(pattern, s_list):
            if c in atow_dic:
                if w != atow_dic[c]:
                    return False
                elif w in wtoa_dic and wtoa_dic[w] != c:
                    return False
            elif w in wtoa_dic:
                return False
            else:
                atow_dic[c] = w
                wtoa_dic[w] = c
        
        return True        

tc = [
        ["abba", "dog cat cat dog", True],
        ["abba", "dog cat cat fish", False],
        ["aaaa", "dog cat cat dog", False],
        ["abba", "dog dog dog dog", False]
    ]

sol = Solution()
for i, [p, s, expected] in enumerate(tc, 1):
    result = sol.wordPattern(p, s)
    print(f"TC {i} is Passed!" if result == expected else f"TC {i} is Failed!")