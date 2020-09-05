# 체육복

def solution(n, lost, reserve):
    n -= len(lost)
    check_lost = {}
    check_reserve = {}
    for i in reserve:
        check_reserve[i] = False

    for i in lost:    
        check_lost[i] = False
        if i in check_reserve:
            n+=1
            check_lost[i] = True
            check_reserve[i] = True
    
    print(check_lost, check_reserve)
  
    for i in lost:
        # if i-1 in check_reserve:
        #     if check_lost[i] == False and  check_reserve[i-1] == False:
        #         check_lost[i] = True
        #         check_reserve[i-1] = True
        #         n += 1
        # if i+1 in check_reserve:
        #     if check_lost[i] == False and check_reserve[i+1] == False:
        #         check_lost[i] = True
        #         check_reserve[i+1] = True
        #         n += 1

        if check_lost[i] == False:
            if i-1 in check_reserve:
                if check_reserve[i-1]==False:
                    check_lost[i] = True
                    check_reserve[i-1] = True
                    n+=1
        if check_lost[i] == False:
            if i+1 in check_reserve:
                if check_reserve[i+1]==False:
                    check_lost[i] = True
                    check_reserve[i+1] = True
                    n+=1

    return n


# 개인적으로 문제풀때 
# 프로그래머스 ide로 풀었는데 에러가 난 곳을 잘못 찾아서 한참 해멨다;;
# 정신 똑바로 차려야겠다 ;; ㅠ
# #
# 겹치는 lost 와 reserver 는 제거
# reserve 기준 +1 or -1 으로 lost 삭제하는 방식으로 동작
# # 
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)