# Pancake Sorting
# BFS -> time limit !
# https://www.youtube.com/watch?v=RJrmP3z6Xh4

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        k = len(A)

        result = []
        # find K -> index K
        # and revsers K
        print(A)
        while k > 0:
            k_index = A.index(k)+1
            #
            front_A = A[:k_index]
            front_A = front_A[::-1]
            back_A = A[k_index:]
            A = front_A + back_A
            #
            front_A = A[:k]
            front_A = front_A[::-1]
            back_A = A[k:]
            A = front_A + back_A
            #
            result.append(k_index)
            result.append(k)
            k -= 1
            

        return result

# # 코드 간결 
# # A[:k].index + 1 로 최적화!
# # A = A[:index][::-1] + A[index:] 연속적으로 진행할떄
# # A[::~~][~:~~:] 으로 할 수 있다 !
# class Solution:
#     def pancakeSort(self, A):
#         N = len(A)
#         ans = []
#         k = N
#         while k > 0 :
#             index = A[:k].index + 1
#             ans.append(index)
#             ans.append(k)
#             A = A[:index][::-1] + A[index:]
#             A = A[:k][::-1] + A[k]
#             k -=1
#         return ans

# # 어차피 2개의 element 를 붙이니
# # res.extend([A,B])
# # 그리고 awesome 해서 따라가기 어렵다;;
# # A = A[:i:-1] 는 i 개부터 reverse 하는것!
# # 그러고 나서 A[i:] 를 더한다!
# # 근대 왜 이렇게함(?!?)
# # 역시나 이해하기 어렵다 !
# class Solution:
#     def pancakeSort(self, A):
#         res = []
#         for x in range(len(A), 1, -1):
#             i = A.index(x)
#             res.extend([i + 1, x])
#             print(A,i, A[:i:-1], A[:i])
#             A = A[:i:-1] + A[:i]
            
#         return res