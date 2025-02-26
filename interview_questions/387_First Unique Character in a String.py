from collections import Counter

class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1)
            - Counter only contains lower alphabet counts(26)
    """
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
            
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        
        return -1        

def run_tests():
    solution = Solution()

    # Test cases: (input string, expected index of first unique character)
    test_cases = [
        ("leetcode", 0),  # 'l' is the first unique character
        ("loveleetcode", 2),  # 'v' is the first unique character
        ("aabb", -1),  # No unique character
        ("abcabc", -1),  # No unique character
        ("z", 0),  # Single character is unique
        ("aaabbc", 5),  # 'c' is the first unique character
        ("aabbccdd", -1),  # No unique character
        ("aabbccd", 6),  # 'd' is the first unique character
        ("abcdefg", 0),  # 'a' is the first unique character
        ("", -1),  # Empty string case
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.firstUniqChar(s)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: \"{s}\"")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()