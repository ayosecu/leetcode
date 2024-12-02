class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(path, t, start):
            if t == 0:
                result.append(list(path))
                return
            elif t < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, t - candidates[i], i)
                path.pop()
        
        backtrack([], target, 0)

        return result

def run_tests():
    solution = Solution()

    # Test case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    result1 = sorted([sorted(x) for x in solution.combinationSum(candidates1, target1)])
    expected1 = sorted([sorted(x) for x in expected1])
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    candidates2 = [2]
    target2 = 1
    expected2 = []
    result2 = solution.combinationSum(candidates2, target2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    candidates3 = [2, 3, 5]
    target3 = 8
    expected3 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result3 = sorted([sorted(x) for x in solution.combinationSum(candidates3, target3)])
    expected3 = sorted([sorted(x) for x in expected3])
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    candidates4 = [1]
    target4 = 0
    expected4 = [[]]
    result4 = solution.combinationSum(candidates4, target4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5
    candidates5 = []
    target5 = 7
    expected5 = []
    result5 = solution.combinationSum(candidates5, target5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()