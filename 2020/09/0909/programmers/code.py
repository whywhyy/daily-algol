# 등굣길
# 
# 계속 안되서 왜 그러지 했는데!
# 가로이동은 i[0] 세로이동은 i[1]  
#     for i in puddles:
#        road[i[1]-1][i[0]-1] = -1
# 
def solution(m, n, puddles):
    answer = 0
    road = [ [0 for j in range(m)] for i in range(n)]
    for i in puddles:
        road[i[1]-1][i[0]-1] = -1


    road[0][0] = 1
    for i in range(n):
        for j in range(m):
            if road[i][j] != 0:
                continue
            elif i == 0:
                road[i][j] = road[i][j-1]
            else:
                if j == 0:
                    road[i][j] = road[i-1][j]
                else:
                    if road[i][j-1] == -1 and road[i-1][j] == -1:
                        road[i][j] = -1
                    else:
                        if road[i][j-1] == -1:
                            road[i][j] = road[i-1][j]
                        elif road[i-1][j] == -1:
                            road[i][j] = road[i][j-1]
                        else:
                            road[i][j] = road[i][j-1] + road[i-1][j]
    if road[n-1][m-1] == -1:
        return 0
    return road[n-1][m-1] % 1000000007
