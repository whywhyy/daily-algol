# 예상 대진표
def solution(n,a,b):
    answer = 1
    '''
    12 -> 1
    34 -> 2

    ....

    99 100 -> 50
    '''
    min_m = min(a,b)
    max_m = max(a,b)

    while max_m % 2 != 0 or min_m+1 != max_m:
        if min_m % 2 == 1:
            min_m += 1
        if max_m % 2 == 1:
            max_m += 1
        min_m /= 2
        max_m /= 2
        answer +=1
    return answer