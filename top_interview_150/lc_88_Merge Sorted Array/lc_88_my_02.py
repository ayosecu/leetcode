"""
    - Time Complexity: O(m + n)
    - Space Complexity: O(1)
    - Note
        - Need to update from the right side (Decreasing Ordered)
        - If nums1 list updated from left, re-ordering would be required.
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Using 3 pointers and copy values from the right (Decrease Ordered)
        p1, p2, p3 = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
        
        # if nums2 remains => copy remains
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1


def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),  # General case
        ([1], 1, [], 0, [1]),                                        # nums2 is empty
        ([0], 0, [1], 1, [1]),                                       # nums1 is empty
        ([2, 0], 1, [1], 1, [1, 2]),                                 # Single element merge
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),   # nums2 smaller than nums1
        ([1, 2, 3, 0, 0, 0], 3, [7, 8, 9], 3, [1, 2, 3, 7, 8, 9]),   # nums2 larger than nums1
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
        nums1_copy = nums1[:]  # Create a copy of nums1 to restore after modification
        solution.merge(nums1_copy, m, nums2, n)
        print(f"Test case {i}: {'Passed' if nums1_copy == expected else 'Failed'}, Result: {nums1_copy}, Expected: {expected}")

# Run the tests
run_tests()