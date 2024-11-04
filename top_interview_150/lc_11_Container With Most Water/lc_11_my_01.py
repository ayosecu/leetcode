class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        
        max_water = 0
        while l < r:
            water = (r - l) * min(height[l], height[r])
            max_water = max(max_water, water)
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                r -= 1
                l += 1
        
        return max_water

tc = [
        [[1,8,6,2,5,4,8,3,7], 49],
        [[1,1], 1]
    ]

sol = Solution()

for i, t in enumerate(tc):
    result = sol.maxArea(t[0])
    assert result == t[1], "TC {} Failed, Expected: {}, Result: {}".format(i+1, t[1], result)
    print(f"TC {i+1} Passed - Result: {result}")