# Contains Duplicate III

# !? 864 MS  -> others avg <= 50 ;; 
# 내방식
# O(nlogk +kn)  
# list -> set => 492MS
import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return None
        
        if len(nums) == 1 or t < 0 or k == 0:
            return False

        if len(nums) <= k:
            nums = sorted(nums)
            for i in range(0,len(nums)-1):
                if abs(nums[i+1] - nums[i]) <= t:
                    return True

        now_sorted = sorted(nums[:k+1])
        for i in range(1, len(now_sorted)):
            if abs(now_sorted[i] - now_sorted[i-1]) <= t:
                return True

        now_sorted = list(set(nums[:k+1]))
        for i in range(k+1 ,len(nums)):
            now_sorted.remove(nums[i-k-1])
            # now_sorted.pop(bisect.bisect(now_sorted,nums[i-k-1]))
            a = bisect.bisect_left(now_sorted, nums[i])
            now_sorted.insert(a,nums[i])

            if a != 0 and a != len(now_sorted)-1:
                if abs(now_sorted[a-1] - now_sorted[a]) <= t or \
                    abs(now_sorted[a+1] - now_sorted[a]) <= t:
                    return True
            else:
                if a == 0:
                    if abs(now_sorted[0]-now_sorted[1]) <= t:
                        return True
                else:
                    if abs(now_sorted[-1] - now_sorted[-2]) <= t:
                        return True    
         return False


# # O(KN) ? 
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
#         size = len(nums)
#         if t == 0 and len(nums) == len(set(nums)):
#             return False
        
#         for i, cur_val in enumerate(nums):
#             # awesome => min (i+k+1, len(nums)) !!!! 
#             # if ~~~ => min (i+k+1, len(nums)) 으로 대체!
#             for j in range(i+1, min(i+k+1, len(nums))):
#                 if abs(cur_val - nums[j]) <= t:
#                     return True
                    
#         return False
            

# # awesome !
# # dict.get(key,value) - value 는 존재하지 않을때 return 값!
# # w + 1 bucket 으로 하여
# # 동일한 버켓이면 무조건 return True!! 왜냐하면 w+1 버켓안에 있다면 최대 차이가 W 임!
# # O(N)? 
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         buckets = {}
#         w = t + 1
#         if t < 0:
#             return False
#         for i in range(len(nums)):
#             temp = nums[i]//w
#             if buckets.get(temp, None) != None:
#                 return True
#             if buckets.get(temp-1, None) and abs(nums[i] - buckets.get(temp-1)) < w:
#                 return True
#             if buckets.get(temp+1, None) and abs(nums[i] - buckets.get(temp+1)) < w:
#                 return True
#             buckets[temp] = nums[i]
#             if i >= k:
#                 del buckets[nums[i-k]//w]
#         return False