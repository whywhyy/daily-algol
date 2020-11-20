# 1626. Best Team With No Conflicts
# 아래 쪽의 -> score 가 낮은애를 포함 할 수있는지 확인!
# dp[i] = max(dp[i], dp[j] + w[i][0] ) # 단 w[j][1] <= w[i][1]
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        w = sorted(list(zip(scores,ages)), key=lambda x: (x[0], x[1]))

        N = len(w)
        dp = [0] * N
        mx = 0
        for i in range(N):
            dp[i] = w[i][0]
            for j in range(i):
                if w[j][1] <= w[i][1]:
                    dp[i] = max(dp[i], dp[j]+w[i][0])
            mx = max(mx, dp[i])
        
        return mx