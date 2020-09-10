# 정수 삼각형

def solution(triangle):
    answer = 0
    for i in triangle:
        if len(i) == 1:
            continue
        n = len(i)-1
        for j in range(len(i)):
            if j == 0:
                triangle[n][j] += triangle[n-1][0]
            elif j == n:
                triangle[n][j] += triangle[n-1][j-1]
            else:
                triangle[n][j] += max(triangle[n-1][j-1], triangle[n-1][j])

    return max(triangle[-1])

# # 내 풀이와 동일
# # 나도 1 부터 시작하려고 했는데 잘안되서 그냥 len(i) 씀!
# # 쓰다가 헷갈려서 시간이 더 걸림 ㅠㅠ 
# def solution(triangle):
#     dp = []
#     for t in range(1, len(triangle)):
#         for i in range(t+1):
#             if i == 0:
#                 triangle[t][0] += triangle[t-1][0]
#             elif i == t:
#                 triangle[t][-1] += triangle[t-1][-1]
#             else:
#                 triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
#     return max(triangle[-1])