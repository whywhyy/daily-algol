# 여행경로
# 어쩌다 보니 pop 으로 잘 되었다;;
# 어쩌다 보니 stack 에 최적화 ;; ㅠ 
from copy import copy, deepcopy
from collections import defaultdict, deque
def solution(tickets):
    tic = defaultdict(lambda: deque([]))
    for i in tickets:
        tic[i[0]].append(i[1])
    
    for i in tic.items():
        tic[i[0]] = sorted(tic[i[0]])

    queue = []
    queue.append(("ICN",["ICN"], tic))
    while queue:
        now, result, now_tic = queue.pop()
        if len(result) == len(tickets) + 1:
            return result
        
        if now_tic[now]:
            prev = ""
            for i in range(len(now_tic[now])-1,-1,-1):
                if prev != now_tic[now][i]:
                    prev = now_tic[now][i]
                    new_tic = deepcopy(now_tic)
                    new_tic[now].pop(i)
                    queue.append((prev, result + [prev], new_tic))
