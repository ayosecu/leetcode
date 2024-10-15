class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_list = s.split(" ")

        if len(pattern) != len(s_list):
            return False           
        
        map_p_s, map_s_p = {}, {}
        for c, w in zip(pattern, s_list):
            if c in map_p_s:
                if map_p_s[c] != w:
                    return False
            else:
                map_p_s[c] = w
            
            if w in map_s_p:
                if map_s_p[w] != c:
                    return False
            else:
                map_s_p[w] = c

        return True 

tc = [
        ["abba", "dog cat cat dog"],
        ["abba", "dog cat cat fish"],
        ["aaaa", "dog cat cat dog"],
        ["abba", "dog dog dog dog"]
    ]

sol = Solution()
for t in tc:
    print(sol.wordPattern(t[0], t[1]))