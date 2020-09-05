# 단속카메라
# #
# 나온곳으로 저장!
# 마찬가지로 다음차량 출발지점 확인! 
def solution(routes):
    answer = 1
    routes = [[min(i),max(i)] for i in routes]
    routes = sorted(routes, key=lambda x : x[0])

    s_now_camera = routes[0][0]
    e_now_camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] <= e_now_camera:
            e_now_camera = min(e_now_camera, routes[i][1])
            continue
        else:
            e_now_camera = routes[i][1]
            answer += 1

    return answer

# # 나온곳 기준으로 sorting!
# # 후 나온곳 보다 출발지점이 크면 +1 
# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30000

#     answer = 0

#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]

#     return answer