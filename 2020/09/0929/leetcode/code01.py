# Subarray Product Less Than K

from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        result = 0

        queue = deque([])
        for i in range(len(nums)):
            num = nums[i]
            if num >= k :
                now_num = 1
                if queue:
                    result += len(queue)*(len(queue)+1) //2
                    queue = []
                continue

            if not queue:
                now_num = num
                queue.append(now_num)
                continue
            
            if queue:
                now_num *= num
                if now_num < k:
                    queue.append(num)
                else:
                    while queue:
                        result += len(queue)
                        div_num = queue.popleft()
                        now_num //= div_num
                        if now_num < k:
                            break
                    queue.append(num)

        result += len(queue)*(len(queue)+1) //2
                        
        return result

# 다들 동일한 방법으로 구현 !
# # 다른 친구들 코드는 왜이리 짧지 
# # 내가 푼방법과 동일 ! 단지 queue 를 안쓰고 변수로 !
# # 현재 값 prod 를 가지고 num 을 곱한다 !
# # prod >= k 이면 prod <k 될때까지 nums[ws] 로 나눈다! ws+=1
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k <= 1: return 0
        
#         prod, count = 1, 0
#         ws = 0
#         for we, num in enumerate(nums):
#             prod = prod * num

#             while prod >= k:               
#                 prod = prod / nums[ws]
#                 ws += 1

#             count += ( we - ws + 1 )
#         return count        

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k == 0:
#             return 0
#         res = 0
#         j = 0
#         prod = 1
#         for i in range(len(nums)):
#             prod *= nums[i]
#             while j <= i and prod >= k:
#                 prod /= nums[j]
#                 j += 1
#             res += i - j + 1
#         return res

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
#         if k<=1:
#             return 0
#         prod=1
#         ans=left=0
#         for right,val in enumerate(nums):
#             prod*=val
#             while(prod>=k):
#                 prod=prod/nums[left]
#                 left+=1
#             ans=ans+right-left+1
#         return ans
       
       
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
                
#         #see soln
#         if k <= 1: return 0
#         prod = 1
#         ans = left = 0
#         for right, val in enumerate(nums):
#             prod *= val
#             while prod >= k:
#                 prod /= nums[left]
#                 left += 1
#             ans += right - left + 1
#         return ans