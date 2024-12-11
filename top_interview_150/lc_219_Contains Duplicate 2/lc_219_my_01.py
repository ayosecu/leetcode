class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i
        
        return False

tc = [ ([1,2,3,1], 3, True), ([1,0,1,1], 1, True), ([1,2,3,1,2,3], 2, False) ]

sol = Solution()
for i, t in enumerate(tc):
    result = sol.containsNearbyDuplicate(t[0], t[1])
    assert result == t[2], "TC {} Failed - Expected: {}, Result: {}".format(i + 1, t[2], result)
    print(f"TC {i + 1} Passed!!")