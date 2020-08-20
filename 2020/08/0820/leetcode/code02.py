# Non-overlapping Intervals
# https://www.youtube.com/watch?v=BTObFnHbD4U
# 흠.. Case 로 경우의 수를 나눈다!
# 경우의 수를 잘 나누면 
# 1. skip 해도 되는 경우의수
# 2. 당연히 하나를 지워야 하는경우의 수
# 3. 잘 생각해보면 지워야하는 경우의수 
# 를 찾을수 있다.
# 잘 생각해보면 지워야 하는 경우의 수를 잘 생각해야한다..(?)..
# 
# 이 문제의 경우 두 선의 관계를 잘 정의하는것이 포인트!

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1 or len(intervals) == 0:
            return 0

        arr = sorted(intervals, key = lambda x : (x[0],x[1]))
        left = 0
        right = 1
        total_count = 0

        while True:
            if right == len(intervals):
                break
            if arr[left][1] <= arr[right][0]:
                left = right
                right += 1
            elif arr[left][1] < arr[right][1]:
                right += 1
                total_count += 1
            elif arr[left][1] >= arr[right][1]:
                left = right 
                right += 1
                total_count += 1

        return total_count

# 겹치면 지우고 아니면 그냥 +1 !?..
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0
#         intervals.sort(key=lambda i: i[1])
#         count = 0
#         prev = intervals[0]
#         for i in range(1, len(intervals)):
#             if prev[1] > intervals[i][0]:
#                 count += 1
#             else:
#                 prev = intervals[i]
#         return count

# 다들 이렇게 풀었다.
# class Solution:
#     def eraseOverlapIntervals(self, intervals):
#         if len(intervals) < 2: return 0
#         intervals.sort(key = lambda x: x[1])
#         cnt, end = 0, intervals[0][1]
#         for i, (s, e) in enumerate(intervals[1:], start = 1):
#             if s < end:
#                 cnt += 1
#             else:
#                 end = e
#         return cnt