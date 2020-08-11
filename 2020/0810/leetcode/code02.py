#  Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        now = len(s)-1
        total = 0
        for i in range(len(s)):
            total += (ord(s[i]) - ord('A') +1) * 26**now
            now -= 1
        return total

# 거꾸로 하느러 계산좀 했는데 
# 그냥 revser를 해서 하나씩 계산해도 좋은것같다.
# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         # ord_A = ord('A')
#         power = 1
#         res = 0
#         for l in reversed(s):
#             res += (ord(l) - 64) * power
#             power *= 26
            
#         return res