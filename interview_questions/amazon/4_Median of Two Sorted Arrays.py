from typing import List

class Solution:
    """
        - Time Complexity: O((m+n)log(m+n)), m = len(nums1), n = len(nums2)
        - Space Complexity: O(m+n), m = len(nums1), n = len(nums2)
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_new = nums1 + nums2
        nums_new.sort()

        n = len(nums_new)

        if n == 0:
            return float(0)
        if n == 1:
            return float(nums_new[0])        

        mid = n // 2
        if n % 2 == 0:
            return (nums_new[mid - 1] + nums_new[mid]) / 2
        else:
            return float(nums_new[mid])


tc = [
        ([1,3], [2], 2.00000),
        ([1,2], [3,4], 2.50000)

]

for i, (nums1, nums2, expected) in enumerate(tc, 1):
    sol = Solution();
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(f"TC {i} Passed!!" if result == expected else f"TC {i} Failed!! - Expected: {expected}, Result: {result}")
