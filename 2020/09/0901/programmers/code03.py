# 구명보트
# 단지 최대의 몸무게로 타야되는줄 알았다 ㅠㅠ
# 최대 2명이니까
# 가장 작은애는 가장 큰애와 탈수있는지 비교하면서 하자!
# 그리고 list 의 pop(0) 은 너무 느리다 ㅠㅠ
# => deque 의 popleft 를 쓰자!
from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                answer +=1
            else:
                people.pop()
                answer+=1
        else:
            people.pop()
            answer += 1
    return answer