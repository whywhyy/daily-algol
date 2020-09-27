# Car Pooling

import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
      trips = sorted(trips, key= lambda x: x[1])
      # end min heap !
      end_heap = []
      now = 0

      for i in trips:
        people, start, end = i
        while end_heap and end_heap[0][0] <= start:  
          end_now , num = heapq.heappop(end_heap)
          now -= num
        
        now += people
        if now > capacity:
          return False
        heapq.heappush(end_heap, (end, people))

      return True

# # 그저 awesome ! 
# # pois.extend([(start, num), (end, -num)]) 후 num_used += num 만 계산 ㄷㄷ;;
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         pois = []
#         for num, start, end in trips:
#             pois.extend([(start, num), (end, -num)])
#         num_used = 0
#         for _, num in sorted(pois):
#             num_used += num
#             if num_used > capacity:
#                 return False
#         return True