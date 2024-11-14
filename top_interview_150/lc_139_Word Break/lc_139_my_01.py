class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[-1]

def run_tests():
    solution = Solution()

    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    expected1 = True
    result1 = solution.wordBreak(s1, wordDict1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    expected2 = True
    result2 = solution.wordBreak(s2, wordDict2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = False
    result3 = solution.wordBreak(s3, wordDict3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    s4 = "aaaaaaa"
    wordDict4 = ["aaaa", "aa"]
    expected4 = False
    result4 = solution.wordBreak(s4, wordDict4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    s5 = ""
    wordDict5 = ["apple", "pen"]
    expected5 = True
    result5 = solution.wordBreak(s5, wordDict5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()