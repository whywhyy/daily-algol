# 큰 수 만들기

# stack 을 이용하여 푸는문제!
# v 같은 협곡을 찾아서 풀었었는데 시간초과..
# #
# stack을 이용하여 append한 값이 이전 append를 처치(?) 해가면서 앞으로 
# 해쳐가는 형태의 문제
def solution(number, k):
    arr_num = list(number)

    stack = []
    # arr_num.pop(0) 을 하니 속도가 ㅠㅠ
    # for 문으로 돌리니 빠르다!
    for i in range(len(arr_num)):
        ele = arr_num[i]
        stack.append(ele)
        while len(stack) > 1 and stack[-2] < stack[-1]:
            stack.pop(-2)
            k -= 1
            if k == 0:
                return "".join(stack + arr_num[i+1:])

    return "".join(stack[:-k])