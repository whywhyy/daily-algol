# 1624. Largest Substring Between Two Equal Characters
from collections import deque
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left = 0
        right = len(s)-1
        visit = set()

        queue = deque()
        queue.append((left,right))

        while queue:
            l,r = queue.popleft()
            if l != r:
                if (l,r) not in visit:
                    visit.add((l,r))
                    if s[l] == s[r]:
                        return r-l-1
                    queue.append((l+1,r))
                    queue.append((l,r-1))

        return -1

# # WOW !
# # awesome 
# # s[i] in mp: ans = max(ans,i-mp[s[i]]-1) !!
# class Solution:
#     def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         mp = {}
#         ans = -1
#         for i in range(len(s)):
#             if s[i] in mp:
#                 ans = max(ans,i-mp[s[i]]-1)
#             else: 
#                 mp[s[i]]=i
#         return ans

# # WOW
# # awesome !
# class Solution:
#     def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         m = collections.defaultdict(list)
#         for i, x in enumerate(s):
#             m[x].append(i)
#         res = -1
#         for x in m:
#             if len(m[x]) >= 2:
#                 # print(x, m[x])
#                 res = max(res, m[x][-1] - m[x][0] - 1)
#         return res

# # 공통적으로 dict 로 O(n) 만에 해결한다!
# class Solution:
#     def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         longest = -1
#         seen = {}
#         for i, c in enumerate(s):
#             seen[c] = seen.get(c, i)
#             longest = max(longest, i - seen[c] - 1)
#         return longest