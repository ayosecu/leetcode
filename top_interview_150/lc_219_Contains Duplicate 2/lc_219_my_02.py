from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(N), N = The number of unique numbers 
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Using dictionaly
        dic = {}

        for i, n in enumerate(nums):
            if n in dic and i - dic[n] <= k:
                return True
            else:
                dic[n] = i
        
        return False

tc = [ ([1,2,3,1], 3, True), ([1,0,1,1], 1, True), ([1,2,3,1,2,3], 2, False) ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.containsNearbyDuplicate(t[0], t[1])
    assert result == t[2], "TC {} Failed - Expected: {}, Result: {}".format(i + 1, t[2], result)
    print(f"TC {i + 1} Passed!!")