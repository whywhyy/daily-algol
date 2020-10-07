#  Remove Covered Intervals
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x : -x[0])
        count = n
        for i in range(n):
            start, end = intervals[i]
            for j in range(i+1,n):
                t_start, t_end = intervals[j]
                if  end <= t_end:
                    count -= 1
                    break
        ㅇ
        return count

# sorting start 는 작은거부터 !, end 는 큰거부터
# x[0]<=right and x[1]>=right right 만 갱신 - 어차피 x[0] 은 항상 크거나 같기때문
# x[0]>right 이면 right, left 둘다 갱신
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            x = intervals[i]
            if x[0]>=left and x[1]<=right:
                count+=1
            elif x[0]<=right and x[1]>=right:
                right = x[1]
            elif x[0]>right:
                left = x[0]
                right = x[1]
                
        return len(intervals)-count