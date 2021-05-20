# 문제링크 #강산
# https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    days = [(math.ceil((100 - p)/s)) for p,s in zip(progresses, speeds)]
    nowMax = days[0]
    count = 0
    answer = []
    for i in days:
        if(i <= nowMax):
            count += 1
        else:
            answer.append(count)
            nowMax = i
            count = 1
    answer.append(count)
    return answer
