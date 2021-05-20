# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42584
import heapq

def solution(prices):
    answer = [0] * len(prices)
    heap = []
    for idx, price in enumerate(prices):
        while(heap):
            (_, hprice, hidx) = heap[0]
            if(price < hprice):
                answer[hidx] = idx - hidx
                heapq.heappop(heap)
                continue
            break
        heapq.heappush(heap, (-price, price, idx))

    while(heap):
        (_, hprice, hidx) = heapq.heappop(heap)
        answer[hidx] = len(prices) - hidx -1
    return answer
