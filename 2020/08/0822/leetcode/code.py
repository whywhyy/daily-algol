# Random Point in Non-overlapping Rectangles
# 완전한 랜덤을 구현하자 !
# 각 사각형마다 확율이 다르다는걸 알아내는 것이 핵심 
import random
from math import sqrt
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.candi = []
        self.all_dot = 0
        for i in rects:
            x1, y1, x2, y2 = i
            self.candi.append((x1,x2,y1,y2, (x2-x1+1) * (y2-y1+1)))
            self.all_dot += (x2-x1+1) * (y2-y1+1)
    
        self.prop = [dots/self.all_dot for _,_,_,_,dots in self.candi]
        now_prop = 0
        for i in range(len(self.prop)):
            now_prop += self.prop[i] 
            self.prop[i] = now_prop


    def pick(self) -> List[int]:        
        result = []
        a = random.uniform(0,1)
        for i in range(len(self.prop)):
            if a <= self.prop[i]:
                x1,x2,y1,y2,_ = self.candi[i]
                break
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return x, y

# # 개선 ver - bisect 
# import bisect       
# import random
# from math import sqrt
# class Solution:

#     def __init__(self, rects: List[List[int]]):
#         self.candi = []
#         self.all_dot = 0
#         for i in rects:
#             x1, y1, x2, y2 = i
#             self.candi.append((x1,x2,y1,y2, (x2-x1+1) * (y2-y1+1)))
#             self.all_dot += (x2-x1+1) * (y2-y1+1)
    
#         self.prop = [dots/self.all_dot for _,_,_,_,dots in self.candi]
#         now_prop = 0
#         for i in range(len(self.prop)):
#             now_prop += self.prop[i] 
#             self.prop[i] = now_prop


#     def pick(self) -> List[int]:        
#         result = []
#         a = random.uniform(0,1)
#         i = bisect.bisect(self.prop, a)
#         x1,x2,y1,y2,_ = self.candi[i]
#         # for i in range(len(self.prop)):
#         #     if a <= self.prop[i]:
#         #         x1,x2,y1,y2,_ = self.candi[i]
#         #         break
#         x = random.randint(x1,x2)
#         y = random.randint(y1,y2)
#         return x, y

# # Your Solution object will be instantiated and called as such:
# # obj = Solution(rects)
# # param_1 = obj.pick()



# # 별도로 확율을 구하지 않고 전체 갯수를 이용한다.
# # 하나의 랜덤한 수로 다 처리해도 되는지 조금 의문이 든다..

# import bisect
# import random

# class Solution:

#     def __init__(self, rects: List[List[int]]):
#         self.rects = rects
#         area = 0
#         self.ranges = [area]
#         for x1, y1, x2, y2 in rects:
#             area += (x2 - x1 + 1) * (y2 - y1 +1)
#             self.ranges.append(area)

#     def pick(self) -> List[int]:
#         n = random.randint(0, self.ranges[-1] - 1)
#         i = bisect.bisect(self.ranges, n)
#         x1, y1, x2, y2 = self.rects[i-1]
#         n -= self.ranges[i-1]
#         width = x2 - x1 + 1
#         return [x1 + n % width, y1 + n // width]