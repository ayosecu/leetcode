"""
    - Time Complexity: O(n*klogk), n = len(strs), k = len(s)
    - Space Complexity: O(n*k), n = len(strs), k = len(s)
    - Note
        - string's sort method => "".join(sorted(s))
        - dictionary values to list => just convert by use list()
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            dic[sorted_s].append(s)

        return list(dic.values())

def run_tests():
    solution = Solution()

    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result1 = solution.groupAnagrams(strs1)
    print(f"Test 1 {'passed' if sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1]) else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: Same strings
    strs2 = ["aaa", "aaa", "aaa"]
    expected2 = [["aaa", "aaa", "aaa"]]
    result2 = solution.groupAnagrams(strs2)
    print(f"Test 2 {'passed' if sorted([sorted(group) for group in result2]) == sorted([sorted(group) for group in expected2]) else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: All same anigram strings
    strs3 = ["abc", "cab", "bac"]
    expected3 = [["abc", "cab", "bac"]]
    result3 = solution.groupAnagrams(strs3)
    print(f"Test 3 {'passed' if sorted([sorted(group) for group in result3]) == sorted([sorted(group) for group in expected3]) else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: No anigram
    strs4 = ["a", "b", "c"]
    expected4 = [["a"], ["b"], ["c"]]
    result4 = solution.groupAnagrams(strs4)
    print(f"Test 4 {'passed' if sorted([sorted(group) for group in result4]) == sorted([sorted(group) for group in expected4]) else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: Including empty strings
    strs5 = ["", "b", ""]
    expected5 = [["", ""], ["b"]]
    result5 = solution.groupAnagrams(strs5)
    print(f"Test 5 {'passed' if sorted([sorted(group) for group in result5]) == sorted([sorted(group) for group in expected5]) else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()