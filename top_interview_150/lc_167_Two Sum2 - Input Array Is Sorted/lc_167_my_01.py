class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1

        while left < right:
            check_sum = numbers[left] + numbers[right]
            if check_sum == target:
                return [left+1, right+1]
            elif check_sum < target:
                left += 1
            elif check_sum > target:
                right -= 1
        
        return []

tc = [
        [[2,7,11,15], 9, [1, 2]],
        [[2,3,4], 6, [1, 3]],
        [[-1,0], -1, [1, 2]]
    ]

sol = Solution()
for i in range(len(tc)):
    result = sol.twoSum(tc[i][0], tc[i][1])
    assert result == tc[i][2], "TC {} Failed - Expected: {}, Result: {}".format(i+1, tc[i][2], result)
    print(f"TC {i+1} Passed!")