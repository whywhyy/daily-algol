# problem : 완주하지 못한 선수

def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for n in range(len(participant)-1):
        if participant[n] == completion[n]:
            continue
        else:
            return participant[n]
    return participant[-1]

"""
# collection Counter 함수 연산 활용하여 접근

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""