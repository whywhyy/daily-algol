# Combination Sum III

from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1,10)]
        com = combinations(arr,k)
        result = [i for i in com if sum(i) == n ]
        return result

# DFS backtracking 
# awesome 
# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         res = []
#         self.dfs(range(1,10), k, n, 0, [], res)
#         return res
#     def dfs(self, nums, k, n, index, path, res):
#         if k < 0 or n < 0: # backtracking 
#             return 
#         if k == 0 and n == 0: 
#             res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)