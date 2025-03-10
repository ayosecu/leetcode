from typing import List

class Solution:
    def findMinMy(self, nums: List[int]) -> int:
        # Binary Search
        # check if mid > and mid + 1 => return val of mid + 1
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left]

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
           
            if nums[-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
    
def run_tests():
    solution = Solution()

    # Test cases: (input array, expected minimum value)
    test_cases = [
        ([3, 4, 5, 1, 2], 1),  # Standard rotation
        ([4, 5, 6, 7, 0, 1, 2], 0),  # Larger array
        ([11, 13, 15, 17], 11),  # Already sorted, no rotation
        ([2, 1], 1),  # Smallest rotated case
        ([1], 1),  # Single element case
        ([5, 1, 2, 3, 4], 1),  # Rotation with different pivot
        ([2, 3, 4, 5, 1], 1),  # Another rotation case
        ([10, 20, 30, 40, 50, 5, 7], 5),  # Minimum in second half
        ([1, 2, 3, 4, 5, 6, 7], 1),  # Already sorted
        ([7, 1, 2, 3, 4, 5, 6], 1),  # Rotation at index 1
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findMin(nums)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"  Input: {nums}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}\n")

# Run the tests
run_tests()