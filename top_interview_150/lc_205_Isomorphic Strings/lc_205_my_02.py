"""
    - Time Complexity: O(n), n = len(s)
    - Space Complexity: O(k + l), k = len(unique characters of s), l = len(unique chracters of t)
    - Note
        - Using one dictionary algorithm needs O(n^2) time complexity and O(k) space complexity.
        - Using two dictionary algorithm need O(n) time complexity and O(k + l) space complexity.
        - Therefore two dictionary algorithm is more better than one dictionary algorithm in general.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic_s_t = {}
        dic_t_s = {}

        for s_ch, t_ch in zip(s, t):
            if s_ch not in dic_s_t:
                dic_s_t[s_ch] = t_ch
            elif dic_s_t[s_ch] != t_ch:
                return False
            
            if t_ch not in dic_t_s:
                dic_t_s[t_ch] = s_ch
            elif dic_t_s[t_ch] != s_ch:
                return False
        
        return True

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ("egg", "add", True),                 # Isomorphic strings
        ("foo", "bar", False),               # Not isomorphic
        ("paper", "title", True),            # Isomorphic strings
        ("badc", "baba", False),             # Inconsistent mapping
        ("abc", "def", True),                # One-to-one mapping
        ("a", "a", True),                    # Single character
        ("ab", "aa", False),                 # Mapping not one-to-one
        ("", "", True),                      # Empty strings
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", True), # Long isomorphic strings
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.isIsomorphic(s, t)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()