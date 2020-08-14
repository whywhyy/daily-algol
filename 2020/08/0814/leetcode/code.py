# Longest Palindrome
from collections import Counter

# delete 할필요 없음..
# one 은 그냥 나중에 return 할때만 한번 사용해도 좋음.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        count = Counter(s)
        one = True
        for i in dict(count):
            if count[i] % 2 == 0:
                total += count[i]
                del count[i]
            else:
                if one:
                    one = False
                    total += 1
                    total += count[i] // 2 *2
                else:
                    total += count[i] // 2 *2 

        return total

# # 
# 그냥 value 만 으로 풀어버리기..
# odd 가 있는지는 처음 0으로 세팅
# return 할때 if 문으로 계산해버림..
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         c = collections.Counter(s)
#         res = odd = 0
#         for value in c.values():
#             if value % 2 == 1:
#                 odd = 1
#             res += value // 2 * 2
#         return res + 1 if odd else res

# # 
# 일단 더하고 odd 로 나중에 한번에 빼버린다.
# odd 가 없을시에는 min 으로 결정 ! 
# from collections import Counter
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         d = Counter(s)
#         odd = ans = 0
        
#         for x in d:
#             if d[x] % 2:
#                 odd += 1
#             ans += d[x]
            
#         return min(ans, ans - odd + 1)