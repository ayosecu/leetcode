"""
    - Time Complexity: O(m + n), m = len(ransomNote), n = len(magazine)
    - Space Complexity: O(k), k => unique characters in magazine
    - Note
        - Use hashmap (dictionary) for counting characters
        - Counter can be increased by 1 through magazine string
        - Counter can be decreased by 1 through ransomNote string
        - When hashmap counter to be negative it returns False
"""
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_m = defaultdict(int)

        for ch in magazine:
            hash_m[ch] += 1
        
        for ch in ransomNote:
            hash_m[ch] -= 1
            if hash_m[ch] < 0:
                return False
        
        return True

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ("a", "b", False),                 # Single letter, cannot construct
        ("aa", "ab", False),               # Not enough 'a' in magazine
        ("aa", "aab", True),               # Can construct
        ("", "anything", True),            # Empty ransom note
        ("abc", "abcdabcd", True),         # Enough letters in magazine
        ("aaa", "aa", False),              # Not enough 'a' in magazine
        ("hello", "ollhe", True),          # Anagram of ransom note exists
        ("xyz", "xxyyzz", True),           # Letters repeated, can construct
        ("test", "", False),               # Empty magazine
    ]

    for i, (ransomNote, magazine, expected) in enumerate(test_cases, 1):
        result = solution.canConstruct(ransomNote, magazine)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()