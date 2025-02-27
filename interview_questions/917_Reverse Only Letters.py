class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n), n = len(s)
    """
    def reverseOnlyLetters(self, s: str) -> str:
        # stack for saving characters -> poping later   
        st = [c for c in s if c.isalpha()]    
        s_list = []
                
        for c in s:
            if c.isalpha():
                s_list.append(st.pop())
            else:
                s_list.append(c)
                
        return "".join(s_list)

    def reverseOnlyLettersTwoPointers(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        S = list(s)

        while l < r:
            if not S[l].isalpha():
                l += 1
            elif not S[r].isalpha():
                r -= 1
            else:
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
        
        return "".join(S)

def run_tests():
    solution = Solution()

    # Test cases: (input string, expected output)
    test_cases = [
        ("ab-cd", "dc-ba"),  # Letters reversed, '-' stays
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),  # Mixed case, letters reversed
        ("Test1ng-Leet=code-Q!", "Qedo1ct-Leet=ngTsT!"),  # Numbers and symbols stay
        ("1234", "1234"),  # No letters, remains unchanged
        ("a", "a"),  # Single letter remains same
        ("-a-", "-a-"),  # Non-letters around letter
        ("ab", "ba"),  # Simple two-letter swap
        ("a-b", "b-a"),  # One letter moves
        ("!@#$%^", "!@#$%^"),  # No letters, remains same
        ("A1B2C3", "C1B2A3"),  # Letters reverse, digits stay
        ("ab-cd-ef", "fe-dc-ba"),  # Multiple letter segments
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.reverseOnlyLetters(s)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: \"{s}\"")
        print(f"  Output: \"{result}\"")
        print(f"  Expected: \"{expected}\"\n")

# Run the tests
run_tests()