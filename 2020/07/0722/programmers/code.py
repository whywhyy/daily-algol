# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    # simple anser
    index = 0
    queue.append((truck_weights[index],answer))
    index += 1

    while len(queue):
        answer += 1
        if (answer - queue[0][1]) == bridge_length:
            queue.pop(0)
        if index != len(truck_weights) and \
            sum(x[0] for x in queue) + truck_weights[index] <= weight:
            queue.append((truck_weights[index],answer))
            index += 1
    answer+=1
    return answer

"""
# 정말 도로처럼 시뮬레이션 한다!..

def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec
"""