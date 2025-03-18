from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(prices)
        - Space Complexity: O(1), total
    """
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                total += prices[i] - prices[i - 1]
        
        return total

TC = [ ([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0) ]        

for i, (p, expected) in enumerate(TC, 1):
    sol = Solution()
    result = sol.maxProfit(p)
    print(f"TC {i} is Passed!" if result == expected else f"TC {i} is Failed!")