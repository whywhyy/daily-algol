# Implement Rand10() Using Rand7()

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            one = rand7()
            if one == 4:
                continue
            else:
                break
        while True:
            two = rand7()
            if two == 6 or two == 7:
                continue
            else:
                break
        odd = [1, 3, 5, 7, 9]
        even = [2, 4, 6, 8, 10]
        if one < 4:
            return odd[two-1]
        else:
            return even[two-1]


# # 최소한의 rand7 을 쓰면서 return 하는 코드 같다 ! 
# # 나의 경우 1/7 의 확율 과 2/7 의 확율로 retry 를 해야된다.
# # 아래의 경우 9/49 AND 3/63 AND 1/21 매우 적은 확율로 retry 를 한다!
# # awesome !
# class Solution:
#     def rand10(self):
#         """
#         :rtype: int
#         """
#         while True:
#             a = rand7()
#             b = rand7()
#             # 1 ~ 40 40가지 , 41 ~ 49 9가지
#             idx = (a-1)*7+b# thus could reach 1-7
#             if idx<=40:# remember this equal
#                 return (idx-1)%10+1
#             # 1 ~ 9
#             # 1 ~ 60 60가지, 61 ~ 63 3가지
#             a = idx -40
#             idx = (a-1)*7+rand7()
#             if idx<=60:
#                 return (idx-1)%10+1
#             a = idx -60
#             # 1 ~ 3
#             # 1 ~ 21  ~~ WOW
#             idx = (a-1)*7+rand7()
#             if idx<=20:
#                 return (idx-1)%10+1