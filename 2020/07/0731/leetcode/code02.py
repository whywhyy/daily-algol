# Task Scheduler

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        c = Counter(tasks)
        c = c.most_common()
    
        while len(c):
            check = set()
            for i in range(n+1):
                if c[0][0] not in check:
                    now = c.pop(0)
                    check.add(now[0])
                    answer += 1
                    if now[1] != 1:
                        c.append((now[0],now[1]-1))
                    if len(c) == 0:
                        break
                else:
                    answer += n+1-i
                    break
            c= sorted(c, key= lambda x : -x[1])

        return answer
        
"""
# 이게 왜 될까 라고 생각해보면
# 위를 구현해 보고 이게 왜 동작하는지 알게된다;;
# 
# 항상 가장 많이 있는 element 를 사용
# 다음 loop 에서도 가장 많이 있는 걸 쓴다!
# 그래서 ret = (maxCount-1)*(n+1)+counter 이게 맞다;;
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        lst = sorted(count.values(), reverse=True)
        maxCount = lst[0]

        counter = 0
        
        for i in range(len(lst)):
            if lst[i]==maxCount: 
                counter+=1
        
        ret = (maxCount-1)*(n+1)+counter
        return max(ret, len(tasks))
"""