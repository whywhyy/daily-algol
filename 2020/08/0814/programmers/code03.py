# 소수 찾기

# range(2,1000000) 
# -> max(num) ** 0.5 로 바꾸면 좋을듯하다.
from itertools import permutations
def solution(numbers):
    answer = 0
    num = []
    for i in range(1,len(numbers)+1):
        num += permutations(numbers,i)
    num = set(int("".join(i)) for i in num)
    
    test_num = [True] * 10000001
    test_num[1] = False
    test_num[0] = False
    for i in range(2, 10000000):
        if test_num[i] :
            go = 10000001 // i
            for j in range(2,go):
                test_num[i*j] = False

    for i in num:
        if test_num[i] == True:
            answer += 1
    return answer

# set 에 union 연산인 | 를 잘 살렸다.
# 에라토스체 *2 만 잘 없애는 코드이다.
# set을 잘 활용했다.
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)
