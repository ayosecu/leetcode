class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        
        dp = [[False] * n for _ in range(n)]

        start, max_len = 0, 0
        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            start = i
        
        return s[start:start + max_len]
    

def run_tests():
    solution = Solution()

    # Test case 1: Basic palindrome in the middle
    s1 = "babad"
    expected1 = ["bab", "aba"]  # Both are valid
    result1 = solution.longestPalindrome(s1)
    print(f"Test 1 {'passed' if result1 in expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: Smallest even-length palindrome
    s2 = "cbbd"
    expected2 = "bb"
    result2 = solution.longestPalindrome(s2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: Single character string
    s3 = "a"
    expected3 = "a"
    result3 = solution.longestPalindrome(s3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: Empty string
    s4 = ""
    expected4 = ""
    result4 = solution.longestPalindrome(s4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: Entire string is a palindrome
    s5 = "abcdedcba"
    expected5 = "abcdedcba"
    result5 = solution.longestPalindrome(s5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6: All characters are the same
    s6 = "aaaa"
    expected6 = "aaaa"
    result6 = solution.longestPalindrome(s6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

    # Test case 7: Multiple palindromes with different lengths
    s7 = "racecarenterelephant"
    expected7 = "racecar"  # Longest palindrome
    result7 = solution.longestPalindrome(s7)
    print(f"Test 7 {'passed' if result7 == expected7 else 'failed'}: Expected {expected7}, Got {result7}")

# Run the tests
run_tests()