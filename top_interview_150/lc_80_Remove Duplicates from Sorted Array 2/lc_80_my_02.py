"""
    - Time Complexity: O(n), n = len(nums)
    - Space Complexity: O(1)
    - Note
        - Two pointers algorithm (writer and current pointers)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        w_ptr, c_ptr = 2, 2
        while c_ptr < len(nums):
            if nums[w_ptr - 2] != nums[c_ptr]:
                nums[w_ptr] = nums[c_ptr]
                w_ptr += 1
            c_ptr += 1
        
        return w_ptr

def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3], 5),   # General case
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3], 7),  # Multiple duplicates
        ([1, 1], [1, 1], 2),                       # Exactly two duplicates
        ([1, 1, 1], [1, 1], 2),                    # More than two duplicates
        ([1, 2, 3], [1, 2, 3], 3),                 # No duplicates
        ([], [], 0),                               # Empty array
        ([1], [1], 1),                             # Single element
    ]

    for i, (nums, expected_array, expected_length) in enumerate(test_cases, 1):
        nums_copy = nums[:]  # Create a copy to avoid modifying the original test case
        result_length = solution.removeDuplicates(nums_copy)
        print(f"Test case {i}: {'Passed' if nums_copy[:result_length] == expected_array and result_length == expected_length else 'Failed'}, Result: {nums_copy[:result_length]}, Expected Array: {expected_array}, Length: {result_length}, Expected Length: {expected_length}")

# Run the tests
run_tests()