class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        return left
            
# Test the searchInsert function
def test_searchInsert():
    solution = Solution()
    
    # Test case 1
    nums = [1, 3, 5, 6]
    target = 5
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 2
    
    # Test case 2
    nums = [1, 3, 5, 6]
    target = 2
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 1
    
    # Test case 3
    nums = [1, 3, 5, 6]
    target = 7
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 4
    
    # Test case 4
    nums = [1, 3, 5, 6]
    target = 0
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 0

    # Test case 5
    nums = [1]
    target = 1
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 0

    # Test case 6
    nums = [3,5,7,9,10]
    target = 8
    print(f"Insert position of {target} in {nums}: {solution.searchInsert(nums, target)}")  # Expected output: 3

    
# Run the test
test_searchInsert()        