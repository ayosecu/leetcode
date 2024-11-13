class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_cnt = 0
        while n >= 5:
            n //= 5
            total_cnt += n

        return total_cnt
    
def run_tests():
    solution = Solution()

    # Test case 1
    n1 = 5
    expected1 = 1
    result1 = solution.trailingZeroes(n1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    n2 = 10
    expected2 = 2
    result2 = solution.trailingZeroes(n2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    n3 = 100
    expected3 = 24
    result3 = solution.trailingZeroes(n3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    n4 = 0
    expected4 = 0
    result4 = solution.trailingZeroes(n4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    n5 = 50
    expected5 = 12
    result5 = solution.trailingZeroes(n5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()