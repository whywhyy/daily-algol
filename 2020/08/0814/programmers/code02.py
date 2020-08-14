# 모의고사

def solution(answers):
    answer = []
    p = ['12345', '21232425', '3311224455']
    result = [0] * len(p)

    for i in range(len(answers)):
        cur_p = [ i%len(char) for char in p ]
        
        for j in range(len(cur_p)):
            if int(p[j][cur_p[j]]) == answers[i]:
                result[j] += 1
    
    return [ i+1 for i in range(len(result)) if max(result)==result[i]]