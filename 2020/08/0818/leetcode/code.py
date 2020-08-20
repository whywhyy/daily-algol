# Distribute Candies to People
# 1 +  2 ... n = n(n+1) // 2
# n+1 +  n+2 ... n+ n  -->  n(3n+1) //2
# 2n+1 + 2n+2
# mul(mul*n +i +i) //2
# ...
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        count_loop = 1
        mul_count = 0
        now_candies = candies
        while now_candies:
            now_sub = (num_people * (count_loop * num_people + 1))/2
            if now_candies - now_sub < 0 :
                now_candies = 0
            else:
                now_candies -= now_sub
                count_loop += 2
                mul_count += 1

        result = [0]*num_people
        if mul_count == 0 :
            for i in range(len(result)):
                if candies - (i+1) <= 0:
                    result[i] += candies
                    return result
                candies -= i+1
                result[i] = i+1    
        
        for i in range(len(result)):
            if mul_count == 1:
                candies -= i+1
                result[i] = i+1         
            else:     
                candies -= ((mul_count)*((mul_count-1)*num_people + i+1 +i+1)) // 2
                result[i] = ((mul_count)*((mul_count-1)*num_people + i+1 +i+1)) // 2


        for i in range(len(result)):
            if candies - ((mul_count)*num_people + i+1) <= 0:
                result[i] += candies
                return result
            result[i] += (mul_count)*num_people + i+1
            candies -= (mul_count)*num_people + i+1




# 당연히 등차수열의 합을 이용해서 푸는건줄알고
# 열심히 나름 최소한의 속도로 풀었더니 
# 그냥 코딩(?)해도 풀리는 문제였다.
# 속도는 가장 빠른축에 속해서 그나마 마음의 위안을 받았다. 
# 수학으로 풀려고 하니 정신을 똑바로(?) 차려야 수식에 안말린다..
#
# class Solution:
#     def distributeCandies(self, candies: int, num_people: int) -> List[int]:
#         a = [0] * num_people
#         i = 0
#         while(candies>0):
#             for j in range(num_people):
#                 i += 1
#                 if i <= candies:
#                     a[j] += i
#                     candies = candies-i
#                 else:
#                     a[j] += candies
#                     candies=0
#         return(a)

# class Solution:
#     def distributeCandies(self, candies: int, num_people: int) -> List[int]:
#         res = [0] * num_people
#         n = 0
        
#         while candies > 0:
#             index = 0
#             for index in range(num_people):
#                 dist_candies = (index + 1) + n * num_people
#                 if candies >= dist_candies:
#                     res[index] += dist_candies
#                     candies -= dist_candies
#                 else:
#                     res[index] += candies
#                     return res
#                 index += 1
#             n += 1
        
#         return res