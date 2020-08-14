# 주식가격
def solution(prices):
    answer = [0]*len(prices)
    queue = []
    for idx, val in enumerate(prices):
        queue.append((idx,val))
        now = [(i,q) for i,q in enumerate(queue) if q[1] > val]

        count = 0
        for i in now:     
            answer[i[1][0]] = idx - i[1][0] 
            queue.pop(i[0]-count)
            count += 1
    for i in queue:
        answer[i[0]] = len(prices) - i[0] -1  
    return answer

"""
# 개선코드 with heapq
# max heap 하는법이 조금 까다로워서
# value 를 - 로 하여 접근하였다.
# 기존 N^2 에서 log 로 줄일수 있을것이다.
import heapq
def solution(prices):
    answer = [0]*len(prices)
    queue = []
    heapq.heapify(queue)
    for idx,val in enumerate(prices):
        heapq.heappush(queue, (-val,idx))
        while len(queue) and -queue[0][0] > val:
            a = heapq.heappop(queue)
            answer[a[1]] = idx - a[1]

    while len(queue):
        a=queue.pop()
        answer[a[1]] = len(prices) -1 - a[1]

    return answer
"""
