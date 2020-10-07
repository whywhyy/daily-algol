# Number of Recent Calls

from collections import deque

class RecentCounter:

    def __init__(self):
        self.candi = deque([])

    def ping(self, t: int) -> int:
        self.candi.append(t)
        row = t - 3000
        # high = t
        while self.candi[0] < row:
            self.candi.popleft()

        return len(self.candi)
        

# class RecentCounter:
#     def __init__(self):
#         self.listQ=[]
#     def ping(self, t: int) -> int:    
#         self.listQ.append(t)
#         while self.listQ:
#             if t-3000 > self.listQ[0]:
#                 self.listQ.pop(0)
#             else:
#                 break 
#         return len(self.listQ)

# 동일한 코드인데 왜 내껀 조금 느릴까 알수없.. 허허 ..
# 알아냈다. 필요없는 연산 때문에 ! 값을 할당하는게 시간이 걸린다.
# immutable 한 값이여서 그런가 보다 ! 
# high = t 가 속도에 문제가 될줄은!
# 필요 없는 연산 및 할당은 하지 말자.
# 
# class RecentCounter:
#     def __init__(self):
#         self.queue = collections.deque()
#     def ping(self, t: int) -> int:
#         while self.queue and self.queue[0] < t-3000:
#             self.queue.popleft()  
#         self.queue.append(t) 
#         return len(self.queue)
