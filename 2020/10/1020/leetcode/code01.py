# Best Time to Buy and Sell Stock IV

# https://www.youtube.com/watch?v=6928FkPhGUA&t=1347s

# Graph
# [3,2,6,5,0,2]
# 3 -> skip buy -> 2,   2   
# 2 -> skip,buy   2 -> skip, sell  
# Graph 의 경우 2^n 임     
# 
# State 기반 - 3 op(skip,buy,sell), 2 state(no stock, bought)
# A -> skip buy -> A,  B
# B -> skip sell -> B, A 
# 
# DP 를 이용하여 transaction에 대한 우선순위를 매긴다!
# - + 를 모두 적용해 앞쪽에서 적용되었다면 뒤쪽에서 적용되어도 동일한 값임!

# 으렵다 ;; 
# ㅠㅠ
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
            if not len(prices) or k == 0:
                return 0 
            # awesome
            if 2*k> len(prices):
                res = 0
                for i in range(1, len(prices)):
                    if(prices[i]>prices[i-1]):
                        res+=(prices[i]-prices[i-1])
                return res
            
            dp  = [0] * (2*k+1)
            dp[0]=-prices[0]

            for i in range(1, len(dp)):
                if i % 2 == 0:
                    dp[i] = float('-inf')
                else:
                    dp[i] = 0

            n = len(prices)
            for i in range(len(prices)):
                for j in range(k*2):
                    if(j==0):
                        dp[j]=max(dp[j],-prices[i])
                    elif (j%2==0):#         //BUY
                        dp[j]=max(dp[j],dp[j-1]-prices[i])
                    else:#                    //SELL
                        dp[j]=max(dp[j],dp[j-1]+prices[i])
                
            return dp[2*k-1]


# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if 2*k >= len(prices): 
#             return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        
#         pnl = [0]*len(prices)
        
#         for _ in range(k):
#             maxd = -prices[0]
#             for i in range(1, len(prices)):
#                 old = pnl[i]
#                 pnl[i] = max(pnl[i-1], maxd+prices[i])
#                 maxd = max(maxd, old-prices[i])
#         return pnl[-1]
        
        
#         for _ in range(k):
#             val = 0
#             for i in range(1, len(pnl)): 
#                 val = max(pnl[i], val + prices[i] - prices[i-1]) 
#                 pnl[i] = max(pnl[i-1], val)
#         return pnl[-1]


# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         K = k
#         n = len(prices)
#         if K >= n / 2:
#             res = 0
#             for i in range(1, n):
#                 res += max(0, prices[i] - prices[i-1])
#             return res
        
#         dp = [[0] * (K + 1) for _ in range(n+1)]
        
#         for k in range(1, K + 1):
#             m = float('-inf')
#             for i in range(1, n + 1):
#                 m = max(m, dp[i][k-1] - prices[i-1])
#                 dp[i][k] = max(dp[i-1][k], m + prices[i-1])
#         return dp[-1][-1]