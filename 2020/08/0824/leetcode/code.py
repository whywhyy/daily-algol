# 못풀어서 정답을 해설보았다.
# O(1)
# https://www.youtube.com/watch?v=Y37WA4advWw&t=171s
import collections
class Trie:
    def __init__(self):
        self.endOfWord = False
        self.children = [None]*26

    # t = self 가능하다.
    def insert(self, s):
        t = self
        for c in s:
            if t.children[ord(c)-ord('a')] == None:
                t.children[ord(c)-ord('a')] = Trie()
            t = t.children[ord(c)-ord('a')]
        t.endOfWord = True

    def search(self, s):
        t = self
        for c in s:
            if t.children[ord(c)-ord('a')] == None: 
                return False
            t = t.children[ord(c)-ord('a')]
            if t.endOfWord: 
                return True
        return False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = collections.deque()
        for w in words:
            self.t.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)
        


#####
# 별도 class 생성없이 구현
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word
        

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node