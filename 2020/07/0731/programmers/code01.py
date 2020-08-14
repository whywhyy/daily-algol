# 이중우선순위큐

def solution(operations):
    answer = []
    nomal = []
    for i in operations:
        a = i.split()
        if a[0] == "D":
            if len(nomal):
                if a[1] == "1":
                    nomal.pop()
                else:
                    nomal.pop(0)
        else:
            val = a[1]
            nomal.append(int(val))
            nomal = sorted(nomal)
    if len(nomal) == 0:
        return [0,0]
    return [nomal[-1],nomal[0]]


"""
# 이렇게 구현하려다 말았는데 결국 이사람은 했다.
# 
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
"""