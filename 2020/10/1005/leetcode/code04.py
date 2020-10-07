# Complement of Base 10 Integer
#import sys
# with out sys
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        #n = bin(N^sys.maxsize)[-(len(bin(N))-2):]
        n = bin(int('1'*(len(bin(N))-2),2)^N)
        return int(n,2)

# # 그냥 만듬! ret 로 !
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         if N == 0:
#             return 1
#         bin_digit = bin(N)[2:]
#         ret = ''
#         for i in bin_digit:
#             if i == '0':
#                 ret += '1'
#             else:
#                 ret += '0'
#         return int(ret, 2)

# # 비트 반전 방법!
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         if N == 0:
#             return 1
        
#         maxx = 1
#         while maxx<=N:
#             maxx= maxx*2
#         return(maxx-N-1)

# # bin 값 만들고
# # 해당 bin 값으로 int 만드는 과정
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         a=bin(N)
#         #print(a,type(a))
#         s=""
#         for i in range(2,len(a)):
#             if a[i]=='1':
#                 s+='0'
#             else:
#                 s+='1'
        
#         while s[0]=='0':
#             s=s[1:]
#             if len(s)==0:
#                 return 0
#         s=s[::-1]
#         #print(s)
#         r=0
#         for i in range(len(s)):
#             r+=int(s[i])*2**i
#         return r