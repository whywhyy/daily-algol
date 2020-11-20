# Minimum Domino Rotations For Equal Row
from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_c = Counter(A)
        b_c = Counter(B)

        candi = []

        for i in range(1,7):
            if len(A) <= a_c[i] + b_c[i]:
                candi.append(i)

        result = -1
        for i in candi:
            count = 0
            for j in range(len(A)):
                if A[j] == i or B[j] == i:
                    if j == len(A) - 1:
                        result = min(len(A)-a_c[i], len(A)-b_c[i])
                else:
                    break
        
        return result

# awesome
# # check = (A[0], B[0]) !? 무조건 둘중 하나가 후보다!!!
# # count 진행 ! 둘다 후보 아니면 break
# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         check = (A[0], B[0])
#         for x in check:            
#             countA = 0
#             countB = 0
#             for i in range(n):
#                 countA += (x == A[i])
#                 countB += (x == B[i])
#                 if x != B[i] and x != A[i]:
#                     break            
#             if i == n-1:
#                 return n - max(countA,countB)
#         return -1


# # for : if  else 가 가능하다니!?
# # B에만 존재하는경우 Count, A에만 존재하는 경우 Count
# # 최소값 return
# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         n = len(A)
#         ans = 10**18
        
#         for i in range(1, 7):
#             cnt = 0
            
#             for j in range(n):
#                 if A[j]!=i:
#                     if B[j]==i:
#                         cnt += 1
#                     else:
#                         break
#             else:
#                 ans = min(ans, cnt)
        
#         for i in range(1, 7):
#             cnt = 0
            
#             for j in range(n):
#                 if B[j]!=i:
#                     if A[j]==i:
#                         cnt += 1
#                     else:
#                         break
#             else:
#                 ans = min(ans, cnt)
        
#         return ans if ans!=10**18 else -1


# # 스왑수로 계산하여 min(swap_A,swap_B) 계산 !
# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         possible_sol = {A[0],B[0]}
        
#         for i in possible_sol:
#             A_swap = 0
#             B_swap = 0
#             flag = 0
#             for j in range(len(A)):
#                 if A[j] == B[j] == i:
#                     pass
#                 elif A[j] == i:
#                     B_swap += 1
#                 elif B[j] == i:
#                     A_swap += 1
#                 else:
#                     flag = 1
#                     break
                    
#             if flag == 0:
#                 return min(A_swap,B_swap)
#         return -1