# First Missing Positive
# 조건을 넣지 않는게 더 빠름;
# 다른 코드들의 의도를 모르겠음;;...
from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = defaultdict(lambda : False)
        for i in nums:
            # if i > 0:
            #     check[i] = True
            check[i] = True
        counter = 1
        while check[counter]:
            counter += 1
        
        return counter

# # simple ! 
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums=list(set(nums))
#         # print(nums)
#         heapify(nums)
#         ans=1
#         while len(nums):
#             curr=heappop(nums)
#             if curr>0:
#                 if curr!=ans:
#                     break
#                 else:
#                     ans+=1
#         return ans

# # 왜!?
# # 무슨코드일까. 모르겠다.. ㅠㅠ
# # nums[nums[i]-1]!=nums[i]
# # nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1] !? swap ?! 
# # 모르게따 ! ! 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(len(nums)):
            while 0<nums[i]<=len(nums) and i > 0 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1

# # simple !
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
        
#         if not nums:
#             return 1
        
#         numSet = set(nums)
        
#         for i in range(len(nums) + 1):
#             if i + 1 not in numSet:
#                 return i + 1
        
#         return 2