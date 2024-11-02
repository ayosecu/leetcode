class Solution(object):
    def lengthOfLongestSubstringFist(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n
        
        l_idx, r_idx = 0, 0
        longest = 1
        while r_idx < n - 1:
            longest = max(longest, r_idx - l_idx + 1)
            if s[r_idx+1] in s[l_idx:r_idx+1]:
                l_idx = s[:r_idx+1].index(s[r_idx+1], l_idx) + 1
            r_idx += 1
        longest = max(longest, r_idx - l_idx + 1)
        return longest

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n
        
        l_idx, longest = 0, 0
        dic = {}
        for r_idx in range(n):
            if s[r_idx] not in dic or dic[s[r_idx]] < l_idx:
                dic[s[r_idx]] = r_idx
                longest = max(longest, r_idx - l_idx + 1)    
            else:
                l_idx = dic[s[r_idx]] + 1
                dic[s[r_idx]] = r_idx

        return longest    

tc = [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3]
    ]

sol = Solution()

for i in range(len(tc)):
    result = sol.lengthOfLongestSubstring(tc[i][0])
    assert result == tc[i][1], "TC:{} - Failed, Exptected: {}, Result: {}".format(i+1, tc[i][1], result)
    print(f"TC {i+1} Passed")
