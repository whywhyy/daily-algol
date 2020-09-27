# Teemo Attacking
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries = sorted(timeSeries)
        if not timeSeries:
            return 0
        result = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration

        for i in range(1, len(timeSeries)):
            now_time = timeSeries[i]
            if now_time > end:
                result += end - start
                start = now_time
                end = now_time + duration
            else:
                end = now_time + duration
        
        result += end - start

        return result

# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         if not timeSeries:return 0
#         timeSeries = [t2 - t1 for t1, t2 in zip(timeSeries, timeSeries[1:])]
#         # 차가 duration 이상이면 duration 만큼!
#         # duration 이하면 t 만 ! 
#         # 마지막 attack 은 duration 만큼!
#         return sum(duration if t >=duration else t for t in timeSeries) + duration

# # 첫 -duration 은 마지막 attack 의 duration을 더하기 위함임 
# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         prev = -duration
#         cum = 0
#         for t in timeSeries:
#             x = t-prev
#             cum += x if x < duration else duration
#             prev = t
#         return cum

# # 위와 동일한 풀이 ! 
# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         if not timeSeries: return 0
#         lasthit = timeSeries[0]
#         poisoned = 0
#         for t in timeSeries[1:]:
#             x = t - lasthit
#             poisoned += x if x < duration else duration
#             lasthit = t
        
#         return poisoned + duration