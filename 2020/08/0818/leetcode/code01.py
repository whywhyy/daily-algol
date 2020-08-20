# Best Time to Buy and Sell Stock III
# DP 가 익숙하지 않다.
# 링크 : https://www.youtube.com/watch?v=0FKn0FSIQYE
# front - 맨앞에서 최소 1번 샀다고 가정.
# back - 맨뒤에는 최소 1번 팔았다고 가정 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        front_buy = [0]*len(prices)
        back_sell = [0]*len(prices)

        now_min = prices[0]
        for i in range(1, len(prices)):
            now_min = min(now_min,prices[i])
            front_buy[i] = max(front_buy[i-1], prices[i]-now_min) 

        now_max = prices[len(prices)-1]
        for i in range(len(prices)-2,0,-1):
            now_max = max(now_max, prices[i])
            back_sell[i] = max(back_sell[i+1], now_max-prices[i])

        return max([back_sell[i] + front_buy[i] for i in range(len(back_sell))])

# # first Buy -> first Sell  -> second buy -> second sell
# https://www.youtube.com/watch?v=gVavspgEHyM
# MAX 로 한다(!?) 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0:
#             return 0
        
#         fb = float('-inf')
#         fs = 0
#         sb = float('-inf')
#         ss = 0
#         for i in range(len(prices)):
#             fb = max(fb, -prices[i])
#             fs = max(fs, fb + prices[i])
#             sb = max(sb, fs-prices[i])
#             ss = max(ss, sb + prices[i])
        
#         return ss
