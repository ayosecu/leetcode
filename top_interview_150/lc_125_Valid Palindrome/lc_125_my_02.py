"""
 - Time Complexity: O(n)
 - Space Complexity: O(1)
 - Algorithm: two pointers
 - Note: Need to memory basic string functions such as isalnum() and lower().
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

tc = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]

for i, (s, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.isPalindrome(s)
    assert result == expected, "TC {} Failed!! - Expected: {}, Result: {}".format(i, expected, result)
    print(f"TC {i} Passed!!")
