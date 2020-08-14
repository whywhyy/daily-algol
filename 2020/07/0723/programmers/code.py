# 탑
"""
#개선전
def solution(heights):
    answer = [0]* len(heights)

    now = []
    for i in range(len(answer)-1,0,-1):
        now.append((heights[i],i))
        res = []
        for j in range(len(now)):
            a = now[j]
            if a[0] < heights[i-1]:
                answer[a[1]]  = i
                res.append(j)
        count = 0
        for k in res:
            now.pop(k-count)
            count += 1
    return answer
"""

import heapq
#개선 with heap
def solution(heights):
    answer = [0]* len(heights)

    now = []
    heapq.heapify(now)
    for i in range(len(answer)-1,0,-1):
        heapq.heappush(now,(heights[i],i))

        while len(now) and now[0][0] < heights[i-1]:
            a = heapq.heappop(now)
            answer[a[1]] = i

    return answer