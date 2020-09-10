# 네트워크
def solution(n, computers):
    answer = 0
    check = [False] * n
    queue = []
    for i in range(n):
        if check[i] == False:
            queue.append(i)
            answer += 1
        while queue:
            now = queue.pop()
            check[now] = True
            for j in range(n): 
                if computers[now][j] == 1:
                    if check[j] == False:
                        queue.append(j)

    return answer