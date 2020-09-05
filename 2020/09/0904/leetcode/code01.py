# Repeated Substring Pattern
# simulation ! 
# % 로 나누어 떨어지는 경우에만 실행!
# 나누어 떨어지는 now_i 만큼씩 짤라서 제공한다.
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            if len(s) % i != 0:
                continue
            now_i = i
            for j in range(now_i, len(s)-now_i+1, now_i):
                before = s[j-now_i:j]
                after = s[j:j+now_i]
                if before == after and j == len(s)-now_i:
                    return True
                if before == after:
                    continue
                else:
                    break

        return False
# # 최소한
# # s = t+t
# # 2s = t + t + t + t
# # cut fornt, end  =  a + t + t + b
# # 그러므로 s in (s+s)[1:-1] 은 맞음! awesome!
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         ds = (s+s)[1:-1]
#         "abab"
#         "abab abab"
#         " bab aba"
#         print(s+s)
#         print(ds)
#         return s in ds

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         return s in (s + s)[1: -1]
        