# 타겟 넘버
def solution(numbers, target):
    
    result = [numbers[0],-numbers[0]]
    for i in range(1, len(numbers)):
        now_result = []
        for j in result:
            now_result.append(j-numbers[i])
            now_result.append(j+numbers[i])
        result = now_result

    return result.count(target)

# # awesome
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)