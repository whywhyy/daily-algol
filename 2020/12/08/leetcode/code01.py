# The kth Factor of n
from collections import deque
import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        mid = int(math.sqrt(n))
        factors = deque()

        if mid == math.sqrt(n):
            factors.append(mid)
            mid -= 1

        for i in range(mid,0,-1):
            if n%i == 0:
                factors.appendleft(i)
                factors.append(n//i)

        if len(factors) < k:
            return -1
        else:
            return factors[k-1]

# 
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        result = -1
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        if(k-1 < len(factors)):
            result = factors[k-1]
        print(factors)
        return result

# i**2 처리로 중복데이터 제거
# 일단 넣고 sort ;;
# if 문 한줄처리 !
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(sqrt(n)) + 1):
            if i**2 == n:
                factors.append(i)
            elif n % i == 0:
                factors.append(i)
                factors.append(n // i)
                
        factors.sort()
        # print(factors)
        return factors[k - 1] if len(factors) >= k else -1