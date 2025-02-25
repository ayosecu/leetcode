from collections import Counter

class Solution:

    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1), alphabet range fixed (26*2)
    """
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        
        exist_one = False
        longest = 0
        for num in s_counter.values():
            if num % 2 == 1:
                exist_one = True
                longest += (num - 1)
            else:
                longest += num
        
        return longest + 1 if exist_one else longest

def run_tests():
    solution = Solution()

    # Test cases: (input string, expected longest palindrome length)
    test_cases = [
        ("abccccdd", 7),  # "dccaccd"
        ("a", 1),  # Single letter palindrome
        ("abc", 1),  # Any one letter can be a palindrome
        ("bb", 2),  # "bb"
        ("aaa", 3),  # "aaa"
        ("cccaaa", 5),  # "cacac"
        ("Aa", 1),  # Case-sensitive check, only one letter used
        ("ababababa", 9),  # Whole string can be rearranged
        ("aabbccddeeffg", 13),  # "aabbccddeeffg" uses all letters
        ("xyzxyzxyz", 7),  # Whole string forms a palindrome
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(s)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: \"{s}\"")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()