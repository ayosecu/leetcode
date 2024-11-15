class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0
        trap_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= l_max:
                    l_max = height[left]
                else:
                    trap_water += l_max - height[left]
                left += 1
            else:
                if height[right] >= r_max:
                    r_max = height[right]
                else:
                    trap_water += r_max - height[right]
                right -= 1
        
        return trap_water

def run_tests():
    solution = Solution()

    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected1 = 6
    result1 = solution.trap(height1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    height2 = [4, 4, 4]
    expected2 = 0
    result2 = solution.trap(height2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    height3 = [5, 4, 3, 2, 1]
    expected3 = 0
    result3 = solution.trap(height3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    height4 = [0, 2, 0]
    expected4 = 0
    result4 = solution.trap(height4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    height5 = [0, 5, 0, 3, 0, 2, 0, 1]
    expected5 = 6
    result5 = solution.trap(height5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6
    height6 = []
    expected6 = 0
    result6 = solution.trap(height6)
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

# Run the tests
run_tests()