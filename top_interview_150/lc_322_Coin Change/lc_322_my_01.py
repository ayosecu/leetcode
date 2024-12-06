class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1
    
def run_tests():
    solution = Solution()

    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    expected1 = 3  # 5 + 5 + 1
    result1 = solution.coinChange(coins1, amount1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    coins2 = [2]
    amount2 = 3
    expected2 = -1
    result2 = solution.coinChange(coins2, amount2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    coins3 = [1]
    amount3 = 0
    expected3 = 0
    result3 = solution.coinChange(coins3, amount3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    coins4 = [1]
    amount4 = 2
    expected4 = 2
    result4 = solution.coinChange(coins4, amount4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    coins5 = [186, 419, 83, 408]
    amount5 = 6249
    expected5 = 20
    result5 = solution.coinChange(coins5, amount5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()