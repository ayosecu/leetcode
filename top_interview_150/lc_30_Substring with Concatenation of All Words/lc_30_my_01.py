from collections import Counter

class Solution:
    def TLE_findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        size_word = len(words[0])
        size_words = len("".join(words))    # window

        def make_set(words):
            s = {}
            for w in words:
                if w not in s:
                    s[w] = 1
                else:
                    s[w] += 1
            return s
        
        i = 0
        while i <= len(s)-size_words:
            window_s = s[i:i+size_words]
            is_sub = 1
            set_words = make_set(words) 
            for j in range(0, len(window_s), size_word):              
                temp_word = window_s[j:j+size_word]
                if temp_word not in set_words or set_words[temp_word] == 0:
                    is_sub = 0
                    break
                else:
                    set_words[temp_word] -= 1
            if is_sub:
                ret.append(i)

            i += 1

        return ret    
        
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        n_words, n_word = len(words), len(words[0])
        n_all_words = n_words * n_word
        word_counter = Counter(words)

        result = []

        for i in range(n_word):
            left, right = i, i
            current_counter = Counter()

            while right + n_word <= len(s):
                word = s[right:right + n_word]
                right += n_word

                if word in word_counter:
                    current_counter[word] += 1

                    while current_counter[word] > word_counter[word]:
                        left_word = s[left:left + n_word]
                        current_counter[left_word] -= 1
                        left += n_word
                    
                    if right - left == n_all_words:
                        result.append(left)
                else:
                    current_counter.clear()
                    left = right
        
        return result

def run_tests():
    solution = Solution()

    # Test case 1
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    expected1 = [0, 9]
    result1 = solution.findSubstring(s1, words1)
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    expected2 = []
    result2 = solution.findSubstring(s2, words2)
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    expected3 = [6, 9, 12]
    result3 = solution.findSubstring(s3, words3)
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4:
    s4 = "foobar"
    words4 = []
    expected4 = []
    result4 = solution.findSubstring(s4, words4)
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5:
    s5 = "wordgoodgoodgoodbestword"
    words5 = ["good"]
    expected5 = [4, 8, 12]
    result5 = solution.findSubstring(s5, words5)
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

# Run the tests
run_tests()