# Add and Search Word - Data structure design

# prefix Tree 를 만들어야한다. 
# 결국 정답을 보았다. 그래도 어렵다;;
# https://www.youtube.com/watch?v=jIPmG51vNDE

class TrieNode:
    def __init__(self):
        self.edges = {}
        self.isEnd = False
    
    def hasEdge(self, char):
        return char in self.edges

    def getEdge(self, char):
        return self.edges[char]

    def getEdges(self):
        return self.edges.keys()

    def addEdge(self,char):
        node = TrieNode()
        self.edges[char] = node
    
    def setIsEnd(self, isEnd):
        self.isEnd = isEnd

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        current = self.root
        
        for char in word:
            if not current.hasEdge(char):
                current.addEdge(char)
            current = current.getEdge(char)
        current.setIsEnd(True)

    def _searchNode(self, word, node):
        if word == "":
            return node.isEnd

        char = word[0]
        if char == "." : 
            for edge in node.getEdges():
                if self._searchNode(word[1:], node.getEdge(edge)):
                    return True
            return False
        else:
            return node.hasEdge(char) and self._searchNode(word[1:],node.getEdge(char))

    def search(self, word):
        return self._searchNode(word, self.root)
        


class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.add(word)
        
    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# # prefix 의 느낌이 아닌
# # 문제만 풀기위한 풀이방법 같지만
# # 생각보다 나쁘지 않아보인다..(?)
# # defaultdict(set) 를 이용하여 log input,
# # 동일한 길이의 데이터가 아주 많아지면 문제가 있을 듯 하다.

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = defaultdict(set)
        

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         self.d[len(word)].add(word)
        

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         m = len(word)
#         for w in self.d[m]:
#             c=0
#             for i in range(m):
#                 if w[i] == word[i] or word[i] == '.':
#                     c+=1
#             if c==m:
#                 return True
#         return False
