class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        set_nums = set(nums)

        longest = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                current_num = num
                current_longest = 1

                while current_num + 1 in set_nums:
                    current_num += 1
                    current_longest += 1
                
                longest = max(longest, current_longest)
        
        return longest


def run_tests():
    solution = Solution()

    # Test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),         # General case
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9), # Long sequence
        ([], 0),                             # Empty array
        ([1], 1),                            # Single element
        ([1, 2, 0, 1], 3),                   # Duplicate elements
        ([10, 5, 3, 11, 4, 6, 9], 4),        # Unordered sequence
        (list(range(100000, 0, -1)), 100000) # Large input (worst case)
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.longestConsecutive(nums)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}, Result: {result}, Expected: {expected}")

# Run the tests
run_tests()