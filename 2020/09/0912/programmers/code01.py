# 가장 먼 노드

from collections import defaultdict, deque
import heapq

# 다익스트라 heap 으로 구현 ! 
def solution(n, edge):
    answer = 0
    
    cost = [float('inf')] * (n+ 1)
    cost[0]= 0
    route = defaultdict(list)
    for i in edge:
        start, end = i
        route[start].append(end)
        route[end].append(start)

    check = [False] * (n + 1)
    queue = []
    heapq.heapify(queue)
    # dis, node
    heapq.heappush(queue, (0,1))
    while queue:
        print(queue)
        dis, node = heapq.heappop(queue)
        if not check[node]:
            check[node] = True
        else:
            continue
        cost[node] = min(cost[node], dis)
        for i in route[node]:
            if not check[i]:
                heapq.heappush(queue, (dis+1, i))

    print(cost)
    return cost.count(max(cost))

