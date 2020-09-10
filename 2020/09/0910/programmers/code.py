# 도둑질

def solution(money):
    answer = 0
    if len(money) == 3:
        return max(money)
    # 1 ~~  0  / 1  0     1,0  0 
    # 0 ~~ 01  / 0  1,0    0   1 
    # 0 ~~  0  / 0  1,0  0 
    # #
    # 00 => 00, 01
    # 01 => 10
    # 10 => 00, 01
    # # 
    # case1
    A_1 = 0  # 00 
    B_1 = money[3] # 01 
    C_1 = money[2] # 10
    for i in range(4,len(money)-1):
        tmp_A, tmp_B, tmp_C = A_1, B_1, C_1
        A_1 = max(tmp_A, tmp_C)
        B_1 = max(tmp_A, tmp_C) + money[i]
        C_1 = tmp_B

    # case 2
    A_2 = 0  # 00 
    B_2 = money[2] # 01 
    C_2 = money[1] # 10
    for i in range(3,len(money)-2):
        tmp_A, tmp_B, tmp_C = A_2, B_2, C_2
        A_2 = max(tmp_A, tmp_C)
        B_2 = max(tmp_A, tmp_C) + money[i]
        C_2 = tmp_B

    A_3 = 0  # 00 
    B_3 = money[2] # 01 
    C_3 = money[1] # 10
    # case 3
    for i in range(3,len(money)-1):
        tmp_A, tmp_B, tmp_C = A_3, B_3, C_3
        A_3 = max(tmp_A, tmp_C)
        B_3 = max(tmp_A, tmp_C) + money[i]
        C_3 = tmp_B
    
    return max(max(A_1,B_1,C_1)+money[0],max(A_2,B_2,C_2)+money[-1], max(A_3,B_3,C_3))


# dp 개념 다시 잡고 풀기 !
# 
def solution(money):
    dp_S = [0] * len(money) # 첫번째 집을 무조건 터는경우 # 1 0 ()   0 
    dp_E = [0] * len(money)# 마지막집을 무조건 터는 경우  0 ()  0 1
    dp_N = [0] * len(money)# 둘다 털지 않는 경우  0 ()  0
    # dp[i] = max(dp[i-1], dp[i-2] + dp[i])
    for i in range(1,len(money)-1):
        if i == 1:
            dp_E[i] = max(dp_E[i-1], dp_S[i-2] + money[i])
            dp_N[i] = max(dp_N[i-1], dp_S[i-2] + money[i])
        elif i == len(money)-2:
            dp_S[i] = max(dp_S[i-1], dp_S[i-2] + money[i])
            dp_N[i] = max(dp_N[i-1], dp_S[i-2] + money[i])
        else:
            dp_S[i] = max(dp_S[i-1], dp_S[i-2] + money[i])
            dp_N[i] = max(dp_N[i-1], dp_N[i-2] + money[i])  
            dp_E[i] = max(dp_E[i-1], dp_E[i-2] + money[i])
    return max(max(dp_S)+money[0], max(dp_E)+money[-1], max(dp_N))
