# 132 Pattern
# https://www.youtube.com/watch?v=8nx5dxFuvLo
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        n = len(nums)
        # n
        min_arr = [float('inf')] * n
        min_arr[0] = nums[0]
        for i in range(1,n):
            min_arr[i] = min(nums[i], min_arr[i-1])
        
        stack = []
        # stack 내부를 스캔하지 않아도 되는이유!?
        # if stack and stack[-1] < now:
        #   return True
        # ? ?  
        # 아 인접한곳에서 무조건 132 패턴이 최소 한개이상 발견되기 때문
        # !!!!
        for i in range(n-1, 0, -1):
            now = nums[i]
            while stack and min_arr[i] >= stack[-1]:
                stack.pop()
            
            if stack and stack[-1] < now:
                return True

            stack.append(now)
            
        return False

        # # n^2
        # s_1 = nums[0]
        # for i in range(n-2):
        #     s_1 = min(s_1, nums[i])
        #     s_2 = nums[i+1]
        #     if s_1 < s_2:
        #         for j in range(i+2, n):
        #             s_3 = nums[j]
        #             if s_3 < s_2 and s_1 < s_3:
        #                 return True
        # return False

# # with min heap 
# # 132 Pattern
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         if len(nums) < 3:
#             return False
        
#         n = len(nums)
#         # n
#         min_arr = [float('inf')] * n
#         min_arr[0] = nums[0]
#         for i in range(1,n):
#             min_arr[i] = min(nums[i], min_arr[i-1])
        
#         # stack = []
#         import heapq
#         stack_heap = []
#         # i = min_arr
#         # j = now 
#         # k = min_heap
#         for i in range(n-1, 0, -1):
#             now = nums[i]
#             while stack_heap and min_arr[i] >= stack_heap[0]:
#                 heapq.heappop(stack_heap)

#             if stack_heap and stack_heap[0] < now:
#                 return True

#             heapq.heappush(stack_heap, now)
#         return False

# # 뒤에 2개를 설정해놓고(?) (stack[-1], third)
# # stack[-1] 은 항상 현재 서치하고있는 리스트의 최대값임 
# # nums[i] 값만 확인!  
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         stack, third = [], float('-inf')
#         for i in range(n-1,-1,-1):
#             if nums[i]< third: 
#                 return True
#             while stack and nums[i]>stack[-1]:
#                 third = stack.pop()
#             stack.append(nums[i])
#         return False

# # 마찬가지 방법인듯!? 동일/
# # 다만 range(n-1,-1,-1) => reversed(nums) 로 더 깔끔하게!
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         stack, s3 = [], -float("inf")
#         for n in reversed(nums):
#             if n < s3: 
#                 return True
#             while stack and stack[-1] < n: 
#                 s3 = stack.pop()
#             stack.append(n)
#         return False