# Remove Duplicate Letters

from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_c = Counter(s)
        result = []
        for i in s:
            while (i not in result) and result and ord(i) <= ord(result[-1]) and s_c[result[-1]] != 0:
                result.pop()
            if i not in result:
                result.append(i)
            s_c[i] -= 1

        return "".join(result)

# i not in result 보다는 seenChar = [False] * 26 로 해도 괜찮았을듯 하다.
# 더 좋은건 해당값의 last index 를 가지고 했으면 더 좋았을것같다.
# #
# #
# # 이미 나왔던 alpha 면 skip
# # 뒤쪽에 나와도 되는 alphabet 이면 삭제 !
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         ht = {}
#         for i, c in enumerate(s):
#             ht[c] = i
#         stack = []
#         for i, c in enumerate(s):
#             if c in stack:
#                 continue
#             while stack and c < stack[-1] and ht[stack[-1]] > i:
#                 stack.pop()
#             stack.append(c)
#             # print(c, stack)
#         return ''.join(stack)

# # result에 존재하면 넣지 않는다!
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         if not s:
#             return
        
#         counts = collections.defaultdict(int)
#         for char in s:
#             counts[char] += 1
            
#         seenChar = [False] * 26
#         stack = []
        
#         for char in s:
            
#             counts[char] -= 1
            
#             if seenChar[ord(char) - ord('a')]:
#                 continue
            
#             seenChar[ord(char) - ord('a')] = True
                
#             while stack and stack[-1] > char and counts[stack[-1]]:
#                 seenChar[ord(stack[-1]) - ord('a')] = False
#                 stack.pop()
                
            
#             stack.append(char)
            
            
            
#         return ''.join(stack)

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
        
#         last_index = {}
        
#         for i, char in enumerate(s):
#             last_index[char] = i
            
#         stack = []
#         used  = set()
        
#         i = 0
#         while i < len(s):
#             curr_char = s[i]
#             if curr_char not in used:
#                 while stack and stack[-1] > curr_char and i < last_index[stack[-1]]:
#                     used.discard(stack.pop())
#                 used.add(curr_char)
#                 stack.append(curr_char)
#             i += 1
        
#         return ''.join(stack)

# # last index 를 이용하여 해곃
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         d={c:i for i,c in enumerate(s)}
#         res=""
#         for i,x in enumerate(s):
#             if x not in res:
#                 while res and  x<res[-1] and i<d[res[-1]]:
#                     res=res[:-1]
#                 res+=x
#         return res
        