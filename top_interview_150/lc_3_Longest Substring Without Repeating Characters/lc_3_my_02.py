class Solution:

    """
        - Time Complexity: O(n), n = len(s)
            - r (right) visits all character once (n)
            - l (left) visits all character less than once (<= n)
            - O(2n) => O(n)
        - Space Complexity: O(1)
            - Dictionary : English Letter + digit + symbols and spaces => Constant
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use Hash(Dictionary)
        # Sliding windows method
        n = len(s)
        if n < 2:
            return n

        dic = {}
        longest = 0
        l, r = 0, 0
        
        while r < n:
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1

            dic[s[r]] = r
            longest = max(longest, r - l + 1)
            r += 1

        return longest

def run_tests():
    solution = Solution()

    # Test cases: (input string, expected longest substring length)
    test_cases = [
        ("abcabcbb", 3),  # "abc" is the longest
        ("bbbbb", 1),  # "b" is the longest
        ("pwwkew", 3),  # "wke" or "kew"
        ("", 0),  # Empty string
        ("abcdef", 6),  # Entire string is unique
        ("abba", 2),  # "ab" or "ba"
        ("tmmzuxt", 5),  # "mzuxt" is the longest
        ("au", 2),  # "au"
        ("dvdf", 3),  # "vdf"
        ("abcdbea", 5),  # "cdbea" is the longest
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.lengthOfLongestSubstring(s)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: \"{s}\"")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()