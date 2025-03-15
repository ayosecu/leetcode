class Solution:
    """
        - Time Complexity: O(logn)
        - Space Complexity: O(logn)
        - Complexity depends on the number of digits of n.
    """
    def isHappy(self, n: int) -> bool:
        # Check number is seen in the set => infinite loop
        check_set = set()
        
        while n != 1:
            cal = 0
            while n > 0:
                remain = n % 10
                cal += (remain * remain)
                n //= 10
            if cal in check_set:
                return False
            else:
                check_set.add(cal)
            n = cal
        
        return True        

tc = [ (19, True), (2, False) ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.isHappy(t[0])
    assert result == t[1], "TC {} Failed - Expected: {}, Result: {}".format(i + 1, t[1], result)
    print(f"TC {i + 1} Passed!!")
