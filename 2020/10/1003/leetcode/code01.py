# Combination Sum
import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [i for i in sorted(candidates) if i <= target] 
        
        result = []

        n = len(candidates)
        queue = []
        # val, idx
        for i in range(len(candidates)):
            queue.append([candidates[i], [candidates[i]],i])
        
        while queue:
            val_sum, val_arr, idx = queue.pop()
            if val_sum == target:
                result.append(val_arr)
                continue
            for i in range(idx ,n):
                try_sum = val_sum + candidates[i]
                if try_sum <= target:
                    new_arr = copy.deepcopy(val_arr)
                    new_arr.append(candidates[i])
                    queue.append([try_sum ,new_arr ,i])
        
        return result

# #  if item>remain: item 더 크면 더이성 candidates 를 탐색할 필요 없으므로 -> break
# # if stack and item<stack[-1]:  stack 은 항상 same 이거나 asc 이므로 ittem < stack[-1]  은 continue 
# # else : DFS(remain-item, stack+[item]) 으로 DFS 진행!
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res=[]
#         candidates=sorted(candidates)        
#         def DFS(remain,stack):
#             if remain == 0:
#                 res.append(stack)
#                 return
#             for item in candidates:
#                 if item>remain:
#                     break
#                 if stack and item<stack[-1]:
#                     continue
#                 else:
#                     DFS(remain-item,stack+[item])
#         DFS(target,[])
#         return res


# # 
# # 종료조건  if remain == 0:  경우 return result.append(path)
# # if candidates[i] > remain  인경우 break
# # else : backtracking(remain - candidates[i], path + [candidates[i]], i)
# # for i in range(index, len(candidates)): 로 index 가 항상 커지는 방향으로만 탐색 ! 
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         def backtracking(remain, path, index):
#             if remain == 0: 
#                 return result.append(path)
#             for i in range(index, len(candidates)):
#                 if candidates[i] > remain: 
#                     break
#                 backtracking(remain - candidates[i], path + [candidates[i]], i)
                    
#         candidates.sort()
#         result = []
#         path = []
#         index = 0
#         backtracking(target, path, index)
        
#         return result