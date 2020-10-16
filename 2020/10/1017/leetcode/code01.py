# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        if not matrix:
            return False

        left = 0
        right = len(matrix)-1
        mid = (left+right)//2

        col = 0
        while left < right:
            if matrix[left][-1] >= target:
                col = left
                break
            if matrix[right][0] <= target:
                col = right
                break

            mid = (left+right)//2
            if matrix[mid][0] <= target and  matrix[mid][-1] >= target:
                col = mid
                break

            if matrix[mid][0] > target:
                right = mid-1
                continue
            if matrix[mid][-1] < target:
                left = mid +1
                continue

        if target in matrix[col]:
            return True
        return False

# # 신박!?
# # 제일 큰값을 확인해가며, 해당 row 에 있는지 확인
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         if(matrix==[]):
#             return 0
#         n=len(matrix)
#         m=len(matrix[0])
#         i=0
#         j=m-1
#         while(i<n and j>=0):
#             if(matrix[i][j]==target):
#                 return True
#             elif(target>matrix[i][j]):
#                 i+=1
#             else:
#                 j-=1
#         return False

# #  nums=matrix[mid//n][mid%n] !?!?
# # 아!? r=m*n-1 로 정의했기에 !
# # Awesome 
# # 동작방식 : 마치 하나의 arr 로 만들어서 동작하는 방식과 동일!!
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix:
#             return 0
        
#         m=len(matrix)
#         n=len(matrix[0])
#         l=0
#         r=m*n-1
        
        
#         while l<=r:
#             mid=(l+r)//2
#             nums=matrix[mid//n][mid%n]
#             if nums==target:
#                 return True
#             elif nums<target:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return False

# # 동작방식 : 마치 하나의 arr 로 만들어서 동작하는 방식과 동일!!
# class Solution:
#     def searchMatrix(self, ma: List[List[int]], target: int) -> bool:
#         if len(ma)>0:
#             n=len(ma)
#             m=len(ma[0])

#             low=0
#             high=n*m-1
#             while low<=high:
#                 mid=low+(high-low)//2
#                 if ma[mid//m][mid%m]==target:
#                     return True
#                 elif ma[mid//m][mid%m]>target:
#                     high=mid-1
#                 elif ma[mid//m][mid%m]<target:
#                     low=mid+1
#             else:
#                 return False
#         else:
#             return False