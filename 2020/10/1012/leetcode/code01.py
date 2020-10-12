# Buddy Strings
from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        count = 0
        idx = 0
        arr = []
        for i,j in zip(A,B):
            if i != j:
                count += 1
                arr.append(idx)
            idx += 1
                
        if count > 2 or count == 1 or len(A) != len(B):
            return False

        if count == 0:
            A = Counter(A)
            for i in A:
                if A[i] >= 2:
                    return True
            return False

        if A[arr[0]] == B[arr[1]] and A[arr[1]] == B[arr[0]]:
            return True
        return False

# # 길이비교 False 거르고, 길이가 길고 종류갯수가 더 적으면 True
# # diff list 저장, 갯수로 거르고, 스왑시 정말 같은지 확인
# class Solution:
#     def buddyStrings(self, A: str, B: str) -> bool:
#         if len(A) != len(B):
#             return False
        
#         if A == B and len(set(A)) < len(A):
#             return True
        
#         diffs = [(a, b) for a, b in zip(A, B) if a!= b]
        
#         return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

# class Solution:
#     def buddyStrings(self, A, B):
#         if len(A) != len(B) or set(A) != set(B): return False       
#         if A == B:
#             return len(A) - len(set(A)) >= 1
#         else:     
#             indices = []
#             counter = 0
#             for i in range(len(A)):
#                 if A[i] != B[i]:
#                     counter += 1
#                     indices.append(i)       
#                 if counter > 2:
#                     return False       
#             return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]