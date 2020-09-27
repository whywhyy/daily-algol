# Majority Element II

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        must = len(nums)//3 + 1
        result = []

        count = Counter(nums)
        for i in count:
            if count[i] >= must:
                result.append(i)
            
        return result

# # 그저 한줄
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         l = len(nums)
#         count = Counter(nums)
#         return [n for n in count if count[n] > l//3]

# # set으로 진행
# # list.count 로 갯수 확인
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         r = len(nums)/3
#         ans = []
#         for e in list(set(nums)):
#             if nums.count(e) > r:
#                 ans.append(e)
                
#         return ans