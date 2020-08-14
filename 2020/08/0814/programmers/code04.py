# 카펫

def solution(brown, yellow):
    x = 0
    y = 0
    for i in range(1,int(yellow**0.5)+1):
        if yellow % i == 0:
            y = i
            x = yellow // i
            if (x+2)*2 + y*2 == brown:
                return [x+2,y+2]