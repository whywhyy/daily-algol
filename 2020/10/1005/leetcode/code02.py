# K-diff Pairs in an Array
import heapq
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        check = set(nums)
        use = set()
        count = 0
        while nums:
            now = heapq.heappop(nums)
            if now not in use:
                use.add(now)
                if k == 0:
                    if nums.count(now) >= 1:
                        count += 1
                else:
                    if now + k in check:
                        count += 1

        return count 

# # Counter 를 이용 !
# # 왜 + k 만 체크하는가 ? - 어차피 n은 n-k 가 찾아주기 때문!
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         ret = 0
#         c = collections.Counter(nums)
        
#         for key in c:
#             if k > 0 and key + k in c:
#                 ret += 1
#             if k == 0 and c[key] > 1:
#                 ret += 1
#         return ret