# Insert Interval

# https://www.youtube.com/watch?v=FuLfL_WhUHI&t=985s

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        # newInterval[0] > intervals[i][1] == skip ! 
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1


        mI = newInterval
        # intervals[i][0] <= newInterval[1]: 
        #   if merge  
        # start : min(mI[0], intervals[i][0])
        # end :  max(mI[1], intervals[i][1])
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            i += 1

        result.append(mI)

        while i<n:
            result.append(intervals[i])
            i += 1

        return result

# newInterval 을 insert
# start 순으로 sort !
# 2개의 직선의 관계 ! 
# front_back < back_front : 그냥 insert!
# front_back > back_back  : front 가 흡수 ! continue
# front_back > back_front : front_back => back_back 으로 번경 !
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals = sorted(intervals, key = lambda x:x[0])
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            left, right = res[-1]
            addLeft, addRight = intervals[i]
            
            if right < addLeft:
                res.append(intervals[i])
            elif right > addRight:
                continue
            else:
                res[-1][1] = addRight
            
        return res

# simple !
# res[-1][1] < st 경우 바로 insert ! res.append([st,end])
# 아닌경우 res[-1][1] = max(res[-1][1], end) 
# awesome
class Solution(object):
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort()

        res = []
        for st,end in intervals:
            if not res or res[-1][1] < st:
                res.append([st,end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res

# left list, right list 를 나눈다 !
# 겹치는 부분은 
# new[0] = min(new[0], interval[0]), 
# new[1] = max(new[1], interval[1])
# 로 성정한다 ! 더 작은걸로 ! new[0], 더 큰거로 new[1]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        new = newInterval
        
        for interval in intervals:
            if interval[1] < new[0]:
                left.append(interval)
            elif interval[0] > new[1]:
                right.append(interval)
            else:
                new[0] = min(new[0], interval[0])
                new[1] = max(new[1], interval[1])
        
        return left + [newInterval] + right
# awesome
# middle 에 들어갈 list 들을 정리
# merge 한다 !
# merge list 는 min(middle[0][0], interval[0])
# max(middle[-1][1], interval[1]) 로 결정 ! 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, middle, right = list(), list(), list()
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                middle.append(interval)
        if middle:
            merged = [
                min(middle[0][0], newInterval[0]),
                max(middle[-1][1], newInterval[1])
            ]
        else:
            merged = newInterval
        return left + [merged] + right