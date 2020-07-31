# K번째수

# def solution(array, commands):
#     answer = []
#     for start,end,k in commands:
#         new = array[start-1:end]
#         new = sorted(new)
#         answer.append(new[k-1])
#     return answer

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 파이토닉하다
# map 함수안에 lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands 를
# 사용하다니 대단하다.
def solution(array, commands):
    answer = []
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))