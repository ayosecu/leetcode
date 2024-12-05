class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        
        half = self.myPow(x, n // 2)
        mul = half * half

        return mul if n % 2 == 0 else mul * x

def run_tests():
    solution = Solution()

    # Test case 1
    x1, n1 = 2.0, 10
    expected1 = 1024.0
    result1 = solution.myPow(x1, n1)
    print(f"Test 1 {'passed' if abs(result1 - expected1) < 1e-9 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    x2, n2 = 2.0, -2
    expected2 = 0.25
    result2 = solution.myPow(x2, n2)
    print(f"Test 2 {'passed' if abs(result2 - expected2) < 1e-9 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    x3, n3 = 2.1, 3
    expected3 = 9.261
    result3 = solution.myPow(x3, n3)
    print(f"Test 3 {'passed' if abs(result3 - expected3) < 1e-9 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    x4, n4 = 2.0, 0
    expected4 = 1.0
    result4 = solution.myPow(x4, n4)
    print(f"Test 4 {'passed' if abs(result4 - expected4) < 1e-9 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    x5, n5 = 1.0, 1000
    expected5 = 1.0
    result5 = solution.myPow(x5, n5)
    print(f"Test 5 {'passed' if abs(result5 - expected5) < 1e-9 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    x6, n6 = 2.0, 31
    expected6 = 2147483648.0
    result6 = solution.myPow(x6, n6)
    print(f"Test 6 {'passed' if abs(result6 - expected6) < 1e-9 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()