class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # with reverse
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

    def reverse(self,arr,start,end):
        n = end-start+1
        for i in range(n//2):
            tmp = arr[start+i]
            arr[start+i] = arr[end-i]
            arr[end-i] = tmp 

# # reverse 방법이 더 좋아보인다! tmp 없이 swap 을 !? 역시 Python!       
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
        
#         self.reverse(nums,0,n-1)
#         self.reverse(nums,0,k-1)
#         self.reverse(nums,k,n-1)
        
#     def reverse(self,nums,l,r):
#         while l<r:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#             r-=1

# # while True 가 가능한이유
# # current == start 인 경우를 고려하기 때문
# # 만약 n % k == 0 인경우 start +=1 , 전체 다 한바퀴 도는경우
# # 둘다 해당됨!
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         count = 0
#         n = len(nums)
#         start = 0
#         while count < n:
#             current = start
#             nxt = (current + k)%n
#             prev = nums[current]
#             while True:
#                 tmp = nums[nxt]
#                 nums[nxt] = prev
#                 count += 1
#                 prev = tmp
#                 current = nxt
#                 nxt = (current + k)%n
#                 if current == start:
#                     start += 1
#                     break
#         return nums


# # arr 만들기!
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         a = nums[len(nums)-k:]
#         a += nums[0: len(nums) - k]
#         nums[:] = a
        
        