class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.child = {}
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.root
        for c in word:
            if c not in ptr.child:
                ptr.child[c] = TrieNode(c)
            ptr = ptr.child[c]
        ptr.is_end = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            ch = word[index]
            if ch == ".":
                for child in node.child.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch in node.child:
                    return dfs(index + 1, node.child[ch])
                else:
                    return False

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDictionary = WordDictionary();
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True
print(wordDictionary.search("bad.")) # return False
