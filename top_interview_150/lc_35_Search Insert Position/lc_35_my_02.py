from typing import List

class Solution:
    """
        - Time Complexity: O(logn), n = len(nums)
        - Space Complexity: O(1)
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
