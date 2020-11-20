# Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
       
        intervals = sorted(intervals, key=lambda x:(x[0],x[1]))

        result = [intervals[0]]
        
        for i in range(1,len(intervals)):
            front, back = result[-1]
            
            start, end = intervals[i]
            if back >= start:
                back = max(back, end)
                result[-1][1] = back
            else:
                result.append([start,end])

        return result

# 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda a: a[0])
        new_intervals = []
        last_interval = intervals[0]
        for i in intervals[1:]:
            if i[0] <= last_interval[1]:
                last_interval = [last_interval[0], max(last_interval[1], i[1])]
            else:
                new_intervals.append(last_interval)
                last_interval = i
        new_intervals.append(last_interval)
        return new_intervals

# 아닌경우만 빼서 append!
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        retVal = []
        
        intervals.sort(key=lambda x: x[0])
        
        for interval in intervals:
            if not retVal or retVal[-1][1] < interval[0]:
                retVal.append(interval)
            else:
                retVal[-1][1] = max(retVal[-1][1], interval[1])
        
        return retVal

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        cur = None
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if cur is not None:
                if x <= cur[1]:
                    if y > cur[1]:
                        cur[1] = y
                else:
                    cur = None
            if cur is None:
                cur = [x, y]
                res.append(cur)
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda a: a[0])
        new_intervals = []
        last_interval = intervals[0]
        for i in intervals[1:]:
            if i[0] <= last_interval[1]:
                last_interval = [last_interval[0], max(last_interval[1], i[1])]
            else:
                new_intervals.append(last_interval)
                last_interval = i
        new_intervals.append(last_interval)
        return new_intervals

class Solution:
    def merge(self,v):
        m=[]
        v.sort(key=lambda x:x[0])
        for i in v:
            if not m or m[-1][1]<i[0]:
                m+=[i]
            else:
                m[-1][1]=max(m[-1][1],i[1])
        return m

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        if len(intervals)==0:
            return ans
        elif len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        beg=intervals[0][0]
        end=intervals[0][1]
        for j in range(1,len(intervals)):
            i=intervals[j]
            if i[1]<=end or i[0]<=end:
                end=max(end,i[1])
            else:
                ans.append([beg,end])
                beg=i[0]
                end=i[1]
        ans.append([beg,end])
        return ans

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return []
        n = len(intervals)
        
        intervals.sort()
        
        res = [intervals[0]]
        
        for i in range(1, n):
            last = res[-1]
            last_start, last_end = last[0], last[1]
            
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            if last_end < cur_start: 
                res.append(intervals[i])
            elif cur_start <= last_end and last_end <= cur_end: 
                res[-1][1] = cur_end
            elif cur_start <= last_end and cur_end <= last_end: 
                continue
                
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        answer = []
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                answer.append([start, end])
                start, end = i[0], i[1]
        answer.append([start, end])
        return answer