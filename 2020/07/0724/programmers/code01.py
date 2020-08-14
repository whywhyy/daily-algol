# 프린터

def solution(priorities, location):
    answer = [0]*len(priorities)
    queue = [(j,i) for i,j in enumerate(priorities)]
    
    #for i in range(len(priorities)):
    #    queue.append((priorities[i],i))
    
    cur = 0
    while len(queue):
        now_max = max(pri for pri,idx in queue)
        now = queue.pop(0)
        if now_max == now[0]:
            cur += 1
            answer[now[1]] = cur
        else:
            queue.append(now)
    return answer[location]


"""
# 한줄로 queue 정의
# any 로 max 함수 대신사용
# 정답이 나오면 바로 return 진행
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
"""