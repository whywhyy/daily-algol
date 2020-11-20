# Permutations II
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(permutations(nums)))

# backtracking 을 잘 익혀두자!!
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return []
        
        counter = collections.Counter(nums)
        
        def backtrack(counter, path, length):
            if len(path) == length:
                res.append(path[:])
                return 
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(counter, path + [num], length)
                    counter[num] += 1
        res = []
        backtrack(counter, [], len(nums))
        return res


# with Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results=[]
        def backtrack(combination,counter):
            if len(combination)==len(nums):
                results.append(combination[:])
                return
            for num in counter:
                if counter[num]>0:
                    combination.append(num)
                    counter[num]-=1
                    backtrack(combination,counter)
                    combination.pop()
                    counter[num]+=1
        backtrack([],Counter(nums))
        return results
                
# sorting
# DFS 처음 요소는 input!
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs(nums, [])
        return res

# sorting 이후
# 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        def permute(n, arr,nums):
            if n == 1:
                for ele in nums:
                    self.ans.append(arr+[ele])
            else:
                for ele in range(len(nums)):
                    if ele > 0 and nums[ele] == nums[ele-1]:
                        continue    
                    permute(n-1, arr+[nums[ele]], nums[:ele]+nums[ele+1:])
                    
        
        self.ans = []
        nums.sort()
        permute(len(nums), [],nums)
        return self.ans

# 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        perms = [[]]
        
        for num in nums:
            next_perms = []
            for prev in perms:
                for i in range(len(prev) + 1):
                    if i > 0 and prev[i - 1] == num:
                        break
                    next_perms.append(prev[:i] + [num] + prev[i:])
            perms = next_perms
        
        return perms