# Image Overlap

#  2976 ms deque 를 써도 그다지 성능향상이 없음!
# 아슬아슬하게 통과 ;; 3000 ms 를 넘기면 통과하지 못하는듯!
# with BFS
from collections import deque

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        count = 0
        # queue = []
        queue = deque()
        a_count = 0
        b_count = 0
        for i in A:
            if i == 1:
                a_count += 1
        for i in B:
            if i == 1:
                b_count += 1
        max_arr = A if a_count >= b_count else B
        min_arr = A if a_count < b_count else B

        check_set = set()
        queue.append((max_arr, min_arr, (0,0)))
        
        while queue:
            # now_max, now_min, move = queue.pop(0)
            now_max, now_min, move = queue.popleft()
            if move in check_set:
                continue
            else:
                check_set.add(move)
    
            now_count = 0
            for a,b in zip(now_max,now_min):
                for i in zip(a,b):
                    if i == (1,1):
                        now_count += 1
            # up
            insert_now_max = now_max[:]
            for i in range(len(insert_now_max)-1):
                insert_now_max [i] = insert_now_max [i+1]
            insert_now_max[-1] = [0]*len(insert_now_max[0])
            one_count = 0
            for i in insert_now_max:
                if 1 in i:
                    queue.append((insert_now_max, now_min, (move[0]+1,move[1])))
                    break
            # down
            insert_now_max = now_max[:]
            for i in range(len(insert_now_max)-1,0,-1):
                insert_now_max [i] = insert_now_max [i-1]
            insert_now_max[0] = [0]*len(insert_now_max[0])
            one_count = 0
            for i in insert_now_max:
                if 1 in i:
                    queue.append((insert_now_max, now_min, (move[0]-1,move[1])))
                    break
            # right
            insert_now_max = now_max[:]
            for i in range(len(insert_now_max)):
                insert_now_max[i] = [0] + insert_now_max[i][:len(insert_now_max[0])-1]
            one_count = 0
            for i in insert_now_max:
                if 1 in i:
                    queue.append((insert_now_max, now_min, (move[0],move[1]+1)))
                    break
            # left
            insert_now_max = now_max[:]
            for i in range(len(insert_now_max)):
                insert_now_max[i] = insert_now_max[i][1:] + [0]
            one_count = 0
            for i in insert_now_max:
                if 1 in i:
                    queue.append((insert_now_max, now_min, (move[0],move[1]-1)))
                    break

            count = max(count, now_count)
        
        return count

# # 340
# # (i,j) 집합을 구해 빼는 이유
# # if 빼서 (0,0) 인경우 움직이지 않아도 매칭되는 경우임
# # if 뺴서 (-1,-1) 인 경우 -1,-1  로 이동해야하는 경우임
# # 즉 A의 한점 => B의 모든 점 ! N**2 으로 언제 매칭되는지 계산!
# class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
#         A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
#         B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
#         print(A,B)
#         counter = collections.Counter((ax - bx, ay - by) for ax, ay in A for bx, by in B)
#         print(counter)
#         return max(counter.values() or [0])

        
# # 228 
# # row 최대가 30 이므로 
# class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
#         N = len(A)
#         LA = [i // N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
#         LB = [i // N * 100 + i % N for i in range(N * N) if B[i // N][i % N]]
#         c = collections.Counter(i - j for i in LA for j in LB)
#         return max(c.values() or [0])