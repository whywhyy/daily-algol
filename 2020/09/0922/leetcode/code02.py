# Unique Paths III

# 804 ms
# others 40ms ~ 100ms ;;
# copy 과정이 있어서 매우 느린듯 하다 ! 
# DFS 가 이럴땐 갑
from collections import Counter
from itertools import chain
import copy
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
      zero = list(chain.from_iterable(grid))
      zero_count = Counter(zero)[0]
      
      new_grid = [[-1 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          new_grid[i+1][j+1] = grid[i][j]
          if grid[i][j] == 1:
            start = [i+1, j+1] 
          if grid[i][j] == 2:
            end = [i+1, j+1]
      
      queue = []
      queue.append([start, zero_count, new_grid])

      result = 0
      while queue:
        now_pos, now_zero, now_grid = queue.pop()
        x, y = now_pos
        if now_pos == end:
          if now_zero == 0: 
            result += 1
          continue
      
        go = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in go:
          go_x, go_y = i
          if now_grid[x+go_x][y+go_y] != -1:
            if now_grid[x+go_x][y+go_y] == 0:
              insert_grid = copy.deepcopy(now_grid)
              insert_grid[x+go_x][y+go_y] = -1
              queue.append([[x+go_x, y+go_y], now_zero-1, insert_grid])
            elif now_grid[x+go_x][y+go_y] == 2:
              insert_grid = copy.deepcopy(now_grid)
              queue.append([[x+go_x, y+go_y], now_zero, insert_grid])

      return result



# 방문 체크를 SET 으로 진행!
# DFS 동작 방법 ! => for : if 종료조건 else 시작조건  add DFS() remove 
# 로 동작시킨다 ! 
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # -1 인곳을 다 뺌 = -1 이 아닌것의 수 
        self.count = m*n - sum(1 for r in range(m) for c in range(n) if grid[r][c] == -1) - 1
        self.res = 0
        def recursive(r,c,record):
            for i,j in ((r+1,c),(r,c-1),(r,c+1),(r-1,c)):
                if 0<=i<m and 0<=j<n and (i,j) not in record:
                    if grid[i][j] == 2:
                        if self.count == len(record):
                            self.res += 1
                    elif grid[i][j] != -1:
                        record.add((i,j))
                        recursive(i,j,record)
                        record.remove((i,j))
                        
        for r in range(m): 
            for c in range(n):
                if grid[r][c] == 1:
                    record = set([(r,c)])
                    recursive(r,c,record)
        return self.res
        