# Power of Four


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 00000000000
        # 00000000100
        # 00000010000
        if num == 1 :
            return True
        if num <=0:
            return False
        count = 0
        for i in str(bin(num)[3:]):
            if i == '0':
                count +=1
            else :
                return False
        if count %2 == 0:
            return True
        return False


# awesome 하다 
# num & num-1 == 0 을 생각하다니 
# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         if num==0:
#             return False
#         # 00000000000
#         # 00000000100
        
#         #   00000010000
#         #   00000001111
#         # & 
#         #   00000000000 awesome
#         return (num & num-1==0) & len(bin(num))class Solution:


# # 1의 갯수 세고 
# # 1의 위치 확인해서 진행함.
# # 이것도 좋은 방법 내방법과 비슷한데
# # 더 깔끔하고 빠름
# def isPowerOfFour(self, num):
#     if num<= 0:
#         return False
#     z = bin(num)[::-1]
#     if z.count('1') > 1:
#         return False
#     p = z.index('1')
#     return p % 2 == 0