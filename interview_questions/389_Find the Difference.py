class Solution:
    """
        - Time Complexity: O(n), n = len(t)
        - Space Complexity: O(1), aschii_sum
    """
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_sum = 0

        i = 0
        while i < len(s):
            ascii_sum += ord(t[i])
            ascii_sum -= ord(s[i])
            i += 1
        ascii_sum += ord(t[i])

        return chr(ascii_sum)
    
def run_tests():
    solution = Solution()

    # Test cases: (s, t, expected extra character)
    test_cases = [
        ("abcd", "abcde", "e"),  # Simple extra character
        ("", "y", "y"),  # Single character added
        ("a", "aa", "a"),  # Duplicate character case
        ("aeiou", "aeioux", "x"),  # Vowel test
        ("abcabc", "abcbacc", "c"),  # Mixed order
        ("xyz", "yxzz", "z"),  # Last letter repeated
        ("hello", "hloleo", "o"),  # Repeated letters
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.findTheDifference(s, t)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: s = \"{s}\", t = \"{t}\"")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()