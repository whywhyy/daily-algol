# Largest Time for Given Digits

# 0 0,1,2
# 1 09 09 03
# 2 0 1 2 3 4 5
# 3 09

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        if (not 0 in A) and (not 1 in A) and (not 2 in A):
            return ""
        
        try_A = permutations(A)    
        try_A = list(try_A)

        total = -1
        for i in try_A:
            a,b,c,d = i
            now_sum = a*1000 + b*100+ c*10 + d
            if now_sum % 100 <= 59:
                if now_sum >= 2000 and 2359 >= now_sum:\
                total = max(total, now_sum) 
                elif now_sum >= 1000 and 1959 >= now_sum:\
                    total = max(total, now_sum)
                elif now_sum >= 0 and 959 >= now_sum:\
                    total = max(total, now_sum)

        if total == -1:
            return ""
        else:
            if total >= 1000:
                result = [str(total//1000), str(total//100%10), ':', \
                            str(total//10%10), str(total%10)]
            else:
                result = ['0', str(total//100%10), ':', \
                            str(total//10%10), str(total%10)]
                print(result)

            return "".join(result)

# 시간 계산을 그냥 말그대로 시간으로 계산해서 하면 되는군!?
# hour < 25 and minute < 60  GOOD
# max(hour*60 +minute) !
# from itertools import permutations
# class Solution:
#     def largestTimeFromDigits(self, A: List[int]) -> str:
#         max_time = -1
#         # enumerate all possibilities, with the permutation() func
#         for h, i, j, k in itertools.permutations(A):
#             hour = h*10 + i
#             minute = j*10 + k
#             if hour < 24 and minute < 60:
#                 max_time = max(max_time, hour * 60 + minute)
        
#         if max_time == -1:
#             return ""
#         else:
#             return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

# class Solution:
#     def largestTimeFromDigits(self, A: List[int]) -> str:
#         largest_time, max_mins = '', -1
        
#         for p in itertools.permutations(A):
#             hours = p[0]*10 + p[1]
#             minutes = p[2]*10 + p[3]
            
#             if hours < 24 and minutes < 60:
#                 total_mins = hours*60 + minutes
                
#                 if total_mins > max_mins:
#                     max_mins = total_mins
#                     largest_time = '{}{}:{}{}'.format(*p)
#         return largest_time