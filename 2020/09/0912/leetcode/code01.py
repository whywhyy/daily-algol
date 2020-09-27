# Maximum Product Subarray
# https://www.youtube.com/watch?v=hJ_Uy2DzE08

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0 for j in range(2)] for i in range(len(nums))]
        
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i][0] = 0
                dp[i][1] = 0
            else:
                dp[i][0] = max(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
                dp[i][1] = min(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])

        return max(max(i) for i in dp)

# # 사실 별도의 DP list 가 필요없으니 매번 ans 에 max 를 저장 !
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         low = nums[0]
#         high = nums[0]
#         ans = nums[0]
#         for i in nums[1:]:
#             low1 = min(i, low*i, high*i)
#             high1 = max(i, low*i, high*i)
#             low, high = low1, high1
#             ans = max(ans, low, high)
#         return ans
