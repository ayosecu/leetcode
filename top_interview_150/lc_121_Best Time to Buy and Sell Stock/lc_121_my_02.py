from typing import List
class Solution:
    """
        - Time Complexity: O(n), n = len(prices)
        - Space Complexity: O(1)
        - Note
            - Brute force approach => O(n^2) => 100000 * 100000 => X
            - Greedy approach => O(n)
                - find min price and find max profit trough iterating
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    
def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),   # Buy on day 2 (price=1), sell on day 5 (price=6)
        ([7, 6, 4, 3, 1], 0),      # No profit, decreasing prices
        ([2, 4, 1], 2),            # Buy on day 1 (price=2), sell on day 2 (price=4)
        ([3, 2, 6, 5, 0, 3], 4),   # Buy on day 2 (price=2), sell on day 3 (price=6)
        ([1, 2], 1),               # Buy on day 1 (price=1), sell on day 2 (price=2)
        ([1, 2, 3, 4, 5], 4),      # Buy on day 1 (price=1), sell on last day (price=5)
        ([3, 3, 3, 3, 3], 0),      # No price change, no profit
        ([1, 10, 1, 10, 1, 10], 9), # Buy on day 1 (price=1), sell on day 2 (price=10)
    ]

    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()