# 단어 변환
# 다른 코드들 봤는데 맘에 안드는 ㅠㅠ
from collections import deque, defaultdict

def solution(begin, target, words):
    queue = deque([])
    queue.append((list(begin), 0))
    check = defaultdict(lambda : None)
    for i in words:
        check[i] = False
    check[begin] = True
    while queue:
        now_str, num = queue.popleft()
        if "".join(now_str) == target:
            return num
        for i in range(len(now_str)):
            if now_str[i] != target[i]:
                for j in range(ord('a'), ord('z')+1):
                    new_arr = now_str[:i] + [chr(j)] +now_str[i+1:]
                    new_str = "".join(new_arr)
                    if new_str in check and not check[new_str]:
                        check[new_str] = True
                        queue.append((new_arr, num+1))
    return 0



