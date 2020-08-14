# 쇠막대기

def solution(arrangement):
    answer = 0
    stack = []

    for idx,val in enumerate(arrangement):
        if len(stack) ==0:
            stack.append((idx,val))
        # Lazer or +1
        else :
            a = stack.pop()
            if a[1] == val:
                stack.append(a)
                stack.append((idx,val))
            else:
                if a[0] + 1 == idx :
                    answer += len(stack)
                else:
                    answer += 1

    return answer

"""
# 껄끄러울수 있는 레이저와 막대기 끝부분 구분을 미리 먼저 처리한다.
# 이 경우 레이져 부분을 찾아 0으로 바꿔 처리 !
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
"""