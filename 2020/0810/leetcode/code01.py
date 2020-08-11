# Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_time = 0
        queue = []
        # all loop
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
       
        while queue:
            x, y, time = queue.pop(0)
            total_time = max(time,total_time)
            # go up
            if x > 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                queue.append((x-1,y,time+1))
            # go down
            if x < len(grid)-1 and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                queue.append((x+1,y,time+1))
            # go left
            if y > 0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                queue.append((x,y-1,time+1))
            # go right
            if y < len(grid[0])-1 and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                queue.append((x,y+1,time+1))
 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return total_time

# #
# COOL!!!
# 내가 작성할때는 if 문으로 그냥 때렸다(?)
# 이코드는 반복되는 작업에 대해서
# for 문 한줄로 처리 하였다.
# in_bound 체크를 if 문 없이 단순 and 연사자 사용!
# 마지막에 1 체크하는 부분도 압권!
# any( 1 in row for row in gird )
# GOOD!
# 정리
# if - if - if -if 문을 대체할수 있는 for문도 고려해보자. 
# 특정 값에대해 하나라도 해당되면 True 를 발산하는 any를 기억해두자
# #
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:

#         m, n = len(grid), len(grid[0])
#         queue = collections.deque()
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 2:
#                     queue.append((i, j, 0))
                    
#         minute = 0
#         while queue:
#             i, j, minute = queue.popleft()
#             for x, y in [(0,1),(1,0),(-1,0),(0,-1)]:
#                 a, b = x+i, y+j
#                 in_bounds = 0 <= a < m and 0 <= b < n
#                 if in_bounds and grid[a][b] == 1:
#                     grid[a][b] = 2
#                     queue.append((a, b, minute+1))
                    
#         return -1 if any(1 in row for row in grid) else minute