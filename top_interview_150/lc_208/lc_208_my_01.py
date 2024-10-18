class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end = True
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_end      

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True      
        
# Your Trie object will be instantiated and called as such:
def run_tests():
    trie = Trie()

    # Test case 1: 단어 삽입 및 검색
    trie.insert("apple")
    result1 = trie.search("apple")  # 단어 "apple"이 트라이에 존재해야 함
    expected1 = True
    print(f"Test 1 {'passed' if result1 == expected1 else 'failed'}: Expected {expected1}, Got {result1}")

    # Test case 2: 접두사 검색
    result2 = trie.startsWith("app")  # 접두사 "app"이 트라이에 존재해야 함
    expected2 = True
    print(f"Test 2 {'passed' if result2 == expected2 else 'failed'}: Expected {expected2}, Got {result2}")

    # Test case 3: 단어가 완전히 일치하지 않으면 False 반환
    result3 = trie.search("app")  # "app"은 아직 완전한 단어로 삽입되지 않음
    expected3 = False
    print(f"Test 3 {'passed' if result3 == expected3 else 'failed'}: Expected {expected3}, Got {result3}")

    # Test case 4: "app" 삽입 후 검색
    trie.insert("app")  # 이제 "app"도 삽입
    result4 = trie.search("app")  # 이제 "app"이 트라이에 존재해야 함
    expected4 = True
    print(f"Test 4 {'passed' if result4 == expected4 else 'failed'}: Expected {expected4}, Got {result4}")

    # Test case 5: 없는 단어 검색
    result5 = trie.search("banana")  # "banana"는 삽입되지 않음
    expected5 = False
    print(f"Test 5 {'passed' if result5 == expected5 else 'failed'}: Expected {expected5}, Got {result5}")

    # Test case 6: 긴 접두사 검색
    trie.insert("banana")
    result6 = trie.startsWith("banan")  # 접두사 "banan"은 트라이에 존재해야 함
    expected6 = True
    print(f"Test 6 {'passed' if result6 == expected6 else 'failed'}: Expected {expected6}, Got {result6}")

    # Test case 7: 접두사가 다른 단어 검색
    result7 = trie.startsWith("bana")  # "bana"도 "banana"의 접두사이므로 True
    expected7 = True
    print(f"Test 7 {'passed' if result7 == expected7 else 'failed'}: Expected {expected7}, Got {result7}")

    # Test case 8: 잘못된 접두사 검색
    result8 = trie.startsWith("bax")  # "bax"는 어떤 단어의 접두사도 아님
    expected8 = False
    print(f"Test 8 {'passed' if result8 == expected8 else 'failed'}: Expected {expected8}, Got {result8}")
    
# Run the tests
run_tests()