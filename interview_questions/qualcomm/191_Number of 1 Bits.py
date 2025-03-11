class Solution:
    """
        - Time Complexity: O(1), n is 32bit integer, so max 32 times iterations.
        - Space Complexity: O(1), count
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        
        return count

tc = [ (11, 3), (128, 1), (2147483645, 30)]
for i, (n, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.hammingWeight(n)
    print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed!! - Expected: {expected}, Result: {result}")