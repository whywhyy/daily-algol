# Find the Difference

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S = Counter(s)
        T = Counter(t)

        for i in T:
            if T[i] != S[i]:
                return i

# 어차피 알파벳 ! 
# count 해서 값다른갓 return
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(97,97+26):
            if s.count(chr(i))!=t.count(chr(i)):
                return chr(i)