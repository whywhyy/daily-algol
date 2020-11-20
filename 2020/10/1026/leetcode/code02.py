# Stone Game IV
# 7112 ms
# n 이 주어지면 사용하자 ;;
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (10**5+1)
        # 1 = True
        # 2 = False -> +ADD Squre number True
        dp[1] = True
        dp[2] = False
        for i in range(1, int(math.sqrt(10**5))+1):
            dp[i*i] = True

        for i in range(2, 10**5+1):
            if dp[i] == False:
                for j in range(1, int(math.sqrt(10**5))+1):
                    if j*j+i < 10**5+1:
                        dp[j*j+i] = True
        
        return dp[n]

# with n 
# 304 ms 
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True

        dp = [False] * (n+1)
        # 1 = True
        # 2 = False -> +ADD Squre number True
        dp[1] = True
        dp[2] = False

        for i in range(1, int(math.sqrt(n))+1):
            dp[i*i] = True

        for i in range(2, n+1):
            if dp[i] == False:
                for j in range(1, int(math.sqrt(n))+1):
                    if j*j+i < n+1:
                        dp[j*j+i] = True
        
        # print(dp[:15])
        return dp[n]

# with type hint
# candidate List 를 사용하여 squre numbers 를 잘 다룸
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp: List[int] = [0] * (n+1)
        candidates: List[int] = []
        for j in range(1, int(math.sqrt(n))+1):
            candidates.append(j*j)
        for i in range(n):
            if not dp[i]:
                for can in candidates:
                    if i + can < n:
                        dp[i+can] = 1
                    elif i + can == n:
                        return 1
        return dp[-1]