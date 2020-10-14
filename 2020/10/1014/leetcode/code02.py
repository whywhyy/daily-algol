# House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(101)]

        if len(nums) <= 3:
            return max(nums)

        # must firtst , must last, Dont both
        for i in range(len(nums)):
            if i == 0:
                dp[0][0] = nums[0]
                continue
            elif i == len(nums)-1:
                dp[i][1] = max(dp[i-1][1], dp[i-2][1]+nums[i])
                continue
            else:
                for j in range(3):
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j]+nums[i])


        return max([max(i) for i in dp])

# NICE
# # 어차피 반복되는 부분 함수로 생성 !
# # prev1, prev2 = max(prev1, prev2 + num), prev1 !?!
# # 이유 : 2개 이전값은 prev2, 이전값은 prev1 으로 저장, prev 가 항상 최대!
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         if n == 0:
#             return 0
#         elif n == 1:
#             return nums[0]
        
#         return max(
#             self.rob_range(nums, 0, n - 1),
#             self.rob_range(nums, 1, n),
#         )
        
#     def rob_range(self, nums, lo, hi):
#         prev1 = prev2 = 0
        
#         for num in nums[lo:hi]:
#             prev1, prev2 = max(prev1, prev2 + num), prev1
            
#         return prev1


# # 함수 생성!
# # func(첫번째 값 제거,마지막 값 제거)
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def rob(nums):
#             now = prev = 0
#             for n in nums:
#                 now, prev = max(now, prev + n), now
#             return now
#         return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
