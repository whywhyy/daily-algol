# Word Break II
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        path = []
        # WOW;; Before Try
        word_set = set()
        for i in wordDict:
            for a in i:
                word_set.add(a)
        for i in s:
            if i not in word_set:
                return []

        self.dfs(s,wordDict,result,0,path)
        return result

    def dfs(self,s,wordDict, result, start,path):
        if start == len(s):
            result.append(" ".join(path))
            return
        now = s[start]
        for i in wordDict:
            if now == i[0] and start+len(i) <= len(s):
                if s[start:start+len(i)] == i:
                    path.append(i)
                    self.dfs(s,wordDict,result,start+len(i),path)
                    path.pop()


# 동작전 DP list 를 확인하여 갈지 안갈지 체크한다.
# class Solution:
#     def __init__(self):
#         self.res = []
        
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         if not s:
#             return [""]
#         wordDict = set(wordDict)
#         dp = self.generateDP(s, wordDict)
#         self.dfs(s, "", dp, 0, wordDict)
#         return self.res
    
#     def generateDP(self, s, word_dict):
#         N = len(s)
#         dp = [False] * (N+1)
#         dp[0] =True
#         for i in range(N):
#             for j in range(i, N+1):
#                 if dp[i] and s[i:j] in word_dict:
#                     dp[j] = True
#         return dp
    
#     def dfs(self, s, path, dp, ind, word_dict):
#         print(path.strip())
#         if dp[ind+len(s)]:
#             if not s:
#                 self.res.append(path.strip())
            
#             for i in range(1, len(s)+1):
#                 if s[:i] in word_dict:
#                     self.dfs(s[i:], path+ " " + s[:i], dp, ind+i, word_dict)