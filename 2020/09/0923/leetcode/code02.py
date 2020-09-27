# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if not prices:
            return 0 
        now_min = prices[0]
        for i in range(1,len(prices)):
            now_min = min(now_min, prices[i])
            result = max(result, prices[i]-now_min)

        return result