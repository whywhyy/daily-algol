# N으로 표현

# N
# want num + - // *
# 5
# 55 /////  5*5 5+5 5//5 5-5
# 555 ////  55*5 55-5 55//5 55+5 5*5 *5 
# 5555 ///  555?5
# 55555 //  5555 ~~
# (5+5) * (5+5) 
from collections import defaultdict
def solution(N, number):
    answer = float('inf')
    result_set = defaultdict(set)
    now_s = 0
    for i in range(1,9):
        now_s = int(str(now_s) + str(N))
        result_set[i].add(now_s)

        for j in range(i-1,i//2-1,-1):
            now_num = i-j
            for k in result_set[j]:
                for l in result_set[now_num]:
                    result_set[i].add(k+l)
                    result_set[i].add(k-l)
                    result_set[i].add(k*l)
                    if l != 0:
                        result_set[i].add(k//l)
        if j in result_set[i]:
            return i
        # for j in result_set[i]:
        #     if j == number:
        #         return i
    
    return -1

# # 
# str * i 로 초기값 정의!
#  
def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1