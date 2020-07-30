# Best Time to Buy and Sell Stock with Cooldown

"""
# https://www.youtube.com/watch?v=pkiJyNijgBw
못풀어서 정답을 봤더니 상태기반으로 풀어버린다.
ㄷㄷ;;
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 : 
            return []
        A = 0
        B = -prices[0]
        C = 0
        for i in range(1,len(prices)):
            tmp = A
            A = max(A, C)
            C = B + prices[i]
            B = max(B,tmp-prices[i])
        
        return max(A,B,C)
