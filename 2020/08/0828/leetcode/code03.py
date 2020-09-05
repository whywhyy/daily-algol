# Minimum Cost For Tickets
# https://leetcode.com/discuss/explore/august-leetcoding-challenge/810806/august-leetcode-challenge-minimum-cost-for-tickets-dynamic-programming-with-explanation

# dp는 마지막 날까지 모두 0으로 초기화 !
# dy 에 해당하지 않으면 dp[i] = dp[i-1] 
# 당일치 사자 -> dp[i-1] + costs[0]
# 아 7일전에 살껄 -> dp[i-7] + costs[1]
# 아 30일 전에 살껄 -> dp[i-30] + costs[2]
# 
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0 for i in range(days[-1]+1)]
        dy = set(days)
        for i in range(days[-1]+1):
            if i not in dy:
                dp[i]=dp[i-1]
            else: 
                dp[i]=min(dp[max(0,i-7)]+costs[1],dp[max(0,i-1)]+costs[0],dp[max(0,i-30)]+costs[2])
        return dp[-1]