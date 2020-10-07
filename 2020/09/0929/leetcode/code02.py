# Word Break

# https://www.youtube.com/watch?v=qYQJOENQScs
# GO TO DP ! 
# awesome
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True
        for i in range(n+1):
            if not dp[i]:
                continue

            for word in wordDict:
                k = len(word)
                if word == s[i:i+k]:
                    dp[i+k] = True
        
        return dp[n]

# # 먼저 wordDict 를 set으로 변경 !
# # s.startwith  WOW!
# # startwith 이면 짜르고 새문자열로 변경 ! 
# # 만들어 본적 없는 str 이면 visited 에 add 및 queue 에 append!
# import collections
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:     
        
#         word_set = set(wordDict)
#         visited = set()
        
#         queue = collections.deque()
#         queue.append(s)
        
#         while queue:
#             s = queue.popleft()
#             for word in word_set:
#                 if s.startswith(word):
#                     new_str = s[len(word):]
#                     if new_str == '':
#                         return True
#                     if new_str not in visited:
#                         queue.append(new_str)
#                         visited.add(new_str)
#         return False

# # dp[j] 가 true 일때 dp[j:i] in wordDict 확인 후 
# # True 이면 dp[i] = True 
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         new_dict = set(wordDict)
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
#         for i in range(1, len(s) + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#                     break
#         return dp[-1]

