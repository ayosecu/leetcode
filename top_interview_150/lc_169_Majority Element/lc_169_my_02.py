"""
    - Time Complexity: O(n)
    - Space Complexity
        - Hash algorithm: O(n)
        - Counter algorithm: O(1)
    - Note
        - Hash algorithm is more easy, but counter algorithm is better due to the space complexity.
"""
from typing import List
from collections import defaultdict

class Solution:
    def majorityElementHash(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
            if dic[num] > half:
                return num
            
        return -1

    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    
tc = [ ([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2) ]

for i, (nums, expected) in enumerate(tc, 1):
    sol = Solution()
    result = sol.majorityElement(nums)
    print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed!!")
