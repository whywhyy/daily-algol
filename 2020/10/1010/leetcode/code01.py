# Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0],x[1]))
        result = 1
        now_point = points[0][1]
        for i in range(1, len(points)):
            start, end = points[i]
            if start > now_point:
                now_point = end
                result += 1
            now_point = min(now_point, end)

        return result

# # sorting ! end 가 작은것 부터 !, start 는 큰것부터 ! 
# class Solution:
#     def findMinArrowShots(self, intervals):
#         if not intervals:
#             return 0
#         last = -sys.maxsize
#         res = 0
#         for left, right in sorted(intervals, key=lambda x: (x[1], -x[0])):
#             if left <= last:
#                 continue
#             else:
#                 res += 1
#                 last = right
#         return res

# # 종료 위치가 작은 것 부터 sorting!
# # point 는 right_bound 와 start 를 비교하며 ans += 1 
# class Solution:
#   def findMinArrowShots(self, points: List[List[int]]) -> int:
#     if not points:
#       return 0
    
#     points.sort(key=lambda x:x[1])
#     _, right_bound = points[0]
#     # print(points)
#     ans = 0
#     for point in points[1:]:
#       if point[0] > right_bound:
#         _, right_bound = point
#         ans += 1
#     return ans + 1

# # 위 와 마찬가지 방법
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         end, arrow = float('-inf'), 0
#         for start_, end_ in sorted(points, key=lambda x: x[1]):
#             if start_ > end:
#                 end = end_
#                 arrow += 1
        return arrow