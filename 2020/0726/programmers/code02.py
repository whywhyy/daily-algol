# 기능개발
# O(N+speed,progress)
# from collections import Counter
# def solution(progresses, speeds):
#     answer = []
#     pair = []
#     for i in range(len(progresses)):
#         pair.append((progresses[i],speeds[i]))

#     count = 1
#     while len(pair):
#         if pair[0][0] >= 100:
#             pair.pop(0)
#             answer.append(count)
#             continue
#         else :
#             for i in range(len(pair)):
#                 pair[i] = (pair[i][0]+pair[i][1], pair[i][1])
#             count += 1
#     new = Counter(answer)
#     return [new[x] for x in new ]


# # 개선코드
# O(N)
def solution(progresses, speeds):
    answer = []
    count = 0
    for p,q in zip(progresses,speeds):
        now = 100 - p
        if now % q == 0:
            now_count = now // q
        else :
            now_count = now // q + 1
        if count < now_count:
            count = now_count
            answer.append(1)
        else :
            answer[-1] += 1


    return answer