"""
Word Frequency Counter
Write a Python function that counts the frequency of words in a given text and returns the top N most common words.

Requirements
	1.	Input: A string of text.
	2.	Output: A dictionary with words as keys and their frequency as values.
	3.	Ignore case sensitivity (e.g., "Hello" and "hello" should be treated as the same word).
	4.	Ignore punctuation (e.g., "it's" and "its" should be treated as "its").
	5.	Return words in descending order of frequency.
	6.	Allow an optional parameter N to return the top N words (default: all words).
"""
import re
from collections import Counter, OrderedDict, defaultdict

"""
    - Time Complexity: O(n + mlogN), n = len(s), m = distinct words count
        - Counter.most_common(N) => O(mlogN)
        - lower(), sub(), split(), Counter() => O(n)
    - Space Complexity: O(n)
        - O(n) => s_lower, s_filter, s_split
        - O(m) => s_counter
        - O(N) => dictionary
"""
def count_freq(s, N=None):
    # to_lower
    s_lower = s.lower()
    s_filter = re.sub(r"[^a-z0-9\s]", "", s_lower)
    s_split = s_filter.split()
    s_counter = Counter(s_split)
    return dict(s_counter) if N is None else dict(s_counter.most_common(N))

"""
    - Time Complexity: O(nlogn), n = len(s)
        - sort => O(nlogn)
        - lower(), split(), for loop => O(n)
    - Space Complexity: O(n)
        - O(n) => s_lower, s_filter, s_split
        - O(m) => dic
        - O(N) => ord_dic
"""
def count_freq_ord_dict(s, N):
    # 1. to lower
    s_lower = s.lower()
    # 2. split s by space
    s_list = s_lower.split()
    
    dic = defaultdict(int)
    for str in s_list:
        temp_str = ""
        # remove puctuation, consider only alphanumeric
        for c in str:            
            if "a" <= c <= "z" or "0" <= c <= "9":
                temp_str += c
        # update dictionary (defaultdict(int))        
        dic[temp_str] += 1

    ord_dic = OrderedDict()
    # sort by descening
    i = 0
    for key, val in sorted(dic.items(), key=lambda item: item[1], reverse=True):           
        ord_dic[key] = val
        i += 1
        if N > 0 and N == i:
            break        
    
    # return N elements
    return ord_dic

def do_test():
    text = "Hello world! Hello everyone."
    expected = {"hello": 2, "world": 1, "everyone": 1}
    assert count_freq(text) == expected, f"Test 1 Failed!"
    print("Test 1 Passed!")

    text = "Apple apple APPLE"
    expected = {"apple": 3}
    assert count_freq(text) == expected, "Test 2 Failed!"
    print("Test 2 Passed!")

    text = "Hello, world! It's a great world."
    expected = {"hello": 1, "world": 2, "its": 1, "a": 1, "great": 1}
    assert count_freq(text) == expected, "Test 3 Failed!"
    print("Test 3 Passed!")

    text = "Version 1.2.3 is better than 1.2"
    expected = {"version": 1, "123": 1, "is": 1, "better": 1, "than": 1, "12": 1}
    assert count_freq(text) == expected, "Test 4 Failed!"
    print("Test 4 Passed!")

    text = ""
    expected = {}
    assert count_freq(text) == expected, "Test 5 Failed!"
    print("Test 5 Passed!")

    text = "test test test test"
    expected = {"test": 4}
    assert count_freq(text) == expected, "Test 6 Failed!"
    print("Test 6 Passed!")

    text = "one two three four five"
    expected = {"one": 1, "two": 1, "three": 1, "four": 1, "five": 1}
    assert count_freq(text) == expected, "Test 7 Failed!"
    print("Test 7 Passed!")

    text = "apple banana apple banana apple orange"
    expected = {"apple": 3, "banana": 2}  # Top 2 words only
    assert count_freq(text, 2) == expected, "Test 8 Failed!"
    print("Test 8 Passed!")

do_test()