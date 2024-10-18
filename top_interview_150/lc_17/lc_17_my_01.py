class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone_map = {
                        "2":"abc", "3":"def", "4":"ghi",
                        "5":"jkl", "6":"mno", "7":"pqrs",
                        "8":"tuv", "9":"wxyz" 
                    }
        result = []

        def backtrack(index, path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            str = phone_map[digits[index]]
            for c in str:
                path.append(c)
                backtrack(index + 1, path)
                path.pop()
                
        backtrack(0, [])
        return result

def run_tests():
    solution = Solution()

    # Test case 1: 입력이 "23"일 때
    digits1 = "23"
    expected1 = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    result1 = sorted(solution.letterCombinations(digits1))
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 입력이 "2"일 때
    digits2 = "2"
    expected2 = sorted(["a", "b", "c"])
    result2 = sorted(solution.letterCombinations(digits2))
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 입력이 "" (빈 문자열)일 때
    digits3 = ""
    expected3 = []
    result3 = solution.letterCombinations(digits3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: 입력이 "9"일 때
    digits4 = "9"
    expected4 = sorted(["w", "x", "y", "z"])
    result4 = sorted(solution.letterCombinations(digits4))
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 입력이 "234"일 때
    digits5 = "234"
    expected5 = sorted([
        "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
        "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
        "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
    ])
    result5 = sorted(solution.letterCombinations(digits5))
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()