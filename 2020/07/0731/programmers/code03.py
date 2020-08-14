# 가장 큰 수

import functools

# 정답을 두개 봤는데
# 두개 다 좋다. 
# a+b - b+a  로 좋은 접근법 같다.
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# # 어차피 3자리니 이것도 좋을듯
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key = lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))