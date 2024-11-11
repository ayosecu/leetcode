from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        search_dic = defaultdict(list)
        word_len = len(beginWord)

        for word in wordList:
            for i in range(word_len):
                search_key = word[:i] + "*" + word[i + 1:]
                search_dic[search_key].append(word)
        
        dq = deque([(beginWord, 1)])
        visited = {beginWord}

        while dq:
            word, count = dq.popleft()

            for i in range(word_len):
                search_key = word[:i] + "*" + word[i + 1:]
            
                for w in search_dic[search_key]:
                    if w == endWord:
                        return count + 1
            
                    if w not in visited:
                        visited.add(w)
                        dq.append((w, count + 1))
            
                search_dic[search_key] = []
        
        return 0

def run_tests():
    solution = Solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5  # hit -> hot -> dot -> dog -> cog (5 step)
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4
    beginWord4 = "hit"
    endWord4 = "cog"
    wordList4 = ["hot", "dot", "tod", "hog", "hop", "cog"]
    expected4 = 4
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

# Run the tests
run_tests()