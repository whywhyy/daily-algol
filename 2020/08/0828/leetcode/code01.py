# Find Right Interval
from collections import defaultdict

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_idx = []
        end_idx = []
        result = [-1]*len(intervals)
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            start_idx.append((i, start))
            end_idx.append((i, end))

        start_idx = sorted(start_idx, key=lambda x : x[1])
        end_idx = sorted(end_idx, key=lambda x : -x[1])
        
        for i in range(len(end_idx)):
            idx, end = end_idx[i]
            if not start_idx:
                break
            s_idx, start = start_idx[-1]
            
            if end > start:
                continue
            else: # end <= start
                if end == start:
                    result[idx] = s_idx
                else: # end < start
                    while True:
                        s_idx, start = start_idx[-1]
                        if len(start_idx) == 1:
                            result[idx] = s_idx
                            break
                        else:
                            if end <= start_idx[-2][1]:
                                start_idx.pop()
                            else:
                                result[idx] = s_idx
                                break 

                

        return result

# # this is 현타코드
# # bisect.bisect_left : 정렬된 순서를 유지하도록 적절한 삽입위치를 찾음
# # 즉 bisect.bisect_left == n 이면 -1 , n-1 이면 n-1 을 insert 
# # res.append() 안에 if 문을 쓸수 있다. 허허..;;
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         l = sorted((v[0],i) for i, v in enumerate(intervals))
#         n = len(intervals)
#         res = []
#         for i in intervals:
#             pos = bisect.bisect_left(l,(i[1],))
#             res.append(l[pos][1] if pos != n else -1 )
#         return res
