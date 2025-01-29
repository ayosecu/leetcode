from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(1)
        - Note
            - rotate can be implemented two reverse operations:
                - Full reverse
                - Each part reversion divided by k partition
    """
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        
        k %= len(nums)
        
        """
        [1, 2, 3, 4, 5, 6, 7] => [7, 6, 5, 4, 3, 2, 1]
        [5, 6, 7] + [1, 2, 3, 4]
        """
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return
    
def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # General case
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),           # Negative numbers
        ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),        # Rotation by full length
        ([1, 2, 3], 5, [2, 3, 1]),                          # Rotation greater than array length
        ([1], 1, [1]),                                      # Single element
        ([1, 2], 0, [1, 2]),                                # No rotation
        ([1, 2], 1, [2, 1]),                                # Small array
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),  # k=0, no change
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        nums_copy = nums[:]  # Create a copy to avoid modifying the original test case
        solution.rotate(nums_copy, k)
        print(f"Test case {i}: {'Passed' if nums_copy == expected else 'Failed'}, Result: {nums_copy}, Expected: {expected}")

# Run the tests
run_tests()