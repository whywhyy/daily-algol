# 조이스틱
# 최적화는 못해도
# 맞긴함..!
def solution(name):
    answer = 0
    for i in name:
        val = ord(i) - ord('A') 
        if val > 13:
            val = 26 - val 
        answer += val
    queue = []
    
    must_visit = []
    for i in range(1, len(name)):
        if name[i] != 'A':
            must_visit.append(i)

    queue.append((0,0,must_visit))
    
    result = float('inf')
    while queue:
        print(queue)
        now, total, visit = queue.pop()
        if total > result:
            continue
        if not visit:
            result = min(answer+total, result)
            continue

        # right
        want_go = visit[0]
        want_now = now
        count = 0
        while want_now != want_go:
            want_now += 1
            count += 1
            if want_now == len(name):
                want_now = 0
        queue.append((want_now, total+count, visit[1:]))

        # left 
        want_go = visit[-1]
        want_now = now
        count = 0
        while want_now != want_go:
            want_now -= 1
            count += 1
            if want_now == -1:
                want_now = len(name)-1
        queue.append((want_now, total+count, visit[:-1]))


    return result
