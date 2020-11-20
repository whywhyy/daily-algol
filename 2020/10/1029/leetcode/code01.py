# Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        stack = []
        for i in nums:
            if not stack:
                stack.append(i)
            else:
                now = stack[-1]
                if now + 1 != i:
                    if len(stack) >= 2:
                        start = stack[0]
                        end = stack[-1]
                        result.append(str(start)+'->'+str(end))
                        stack = []
                    else:
                        result.append(str(stack[0]))
                        stack = []
                stack.append(i)
        
        if len(stack) >= 2:
            result.append(str(stack[0])+'->'+str(stack[-1]))
        else:
            result.append(str(stack[0]))

        return result

# if i-1 not in nums 로 시작지점 체크
# 및 마지막점까지 확인후 res.append
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        for i in nums:
            if i-1 not in nums:
                last =i+1
                while last in nums:
                    last+=1
                if i == last-1:
                    res.append(str(i))
                else:
                    res.append(str(i)+"->"+str(last-1))
        return res

# 별도의 temp 를 답는 arr list 로 해결!
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []: return []
        if len(nums) == 1: return [str(nums[0])]
        arr = []
        temp = [nums[0]]
        for i in range(1,len(nums)):  
            if nums[i] - nums[i-1] == 1:
                temp.append(nums[i])
            else:
                arr.append(temp)
                temp = [nums[i]]
        arr.append(temp)
        result = []
        for c in arr:
            if c[0] != c[-1]:
                result.append(str(c[0])+'->'+str(c[-1]))
            else:
                result.append(str(c[0]))
        return result

# index 를 이용해서 해결!
# 가장 좋은 방법 인듯!
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        return res