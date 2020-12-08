# Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        result = [[0] * n for i in range(n)]
        # 4 4 4 3 3 2 2
        
        row = 0
        col = 0 
        result[row][col] = 1
        now_n = 1
        for i in range(n-1):
            # go right
            col += 1
            now_n += 1
            result[row][col] = now_n
            

        for i in range(n-1):
            # go down
            row += 1
            now_n += 1
            result[row][col] = now_n
        
        for i in range(n-1):
            # go left
            col -= 1
            now_n += 1
            result[row][col] = now_n

        count_n = n
        count_n -= 2

        up_right = True
        # down_left = False
        while count_n:
            if up_right:
                for i in range(count_n):
                    now_n += 1
                    row -= 1
                    result[row][col] = now_n

                for i in range(count_n):
                    now_n += 1
                    col += 1
                    result[row][col] = now_n

                up_right = False
            else:
                for i in range(count_n):
                    now_n += 1
                    row += 1
                    result[row][col] = now_n

                for i in range(count_n):
                    now_n += 1
                    col -= 1
                    result[row][col] = now_n
                up_right = True

            count_n -= 1
        
        return result

# 오른쪽, 아래, 왼쪽, 위 ! 
# 방향을 바꿔가며 진행!
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        iMax = n
        jMax = n
        ans = [[None for j in range(n)] for i in range(n)]
  
        ansLen = n*n
        cunt = 1
        dj = [1, 0, -1, 0]
        di = [0, 1, 0, -1]
        k = 0
        i = 0
        j = 0
        iCount = 1
        jCount = 2
        # iMax += 1
        jMax += 1
        while cunt <= ansLen:
            # print(i, j, iCount, jCount, iMax, jMax)
            # print(i, j)
            ans[i][j] = cunt
            if iCount == iMax and di[k] != 0:
                iMax -= 1
                iCount = 1
                k = (k + 1)%4
            elif dj[k] != 0 and jCount == jMax:
                jMax -= 1
                jCount = 1
                k = (k + 1)%4
            iCount += abs(di[k])
            jCount += abs(dj[k])
            i += di[k]
            j += dj[k]
            cunt += 1
        return ans

# awesome
# 오른쪽,아래,왼쪽,위 를 yield 로 처리 !!
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for x in range(n)]
        def getidx(n):
            if n == 1:
                yield 0,0
            else:
                for i in range(n):
                    yield 0, i
                for i in range(1,n-1):
                    yield i, n-1
                for i in range(n-1, -1, -1):
                    yield n-1, i
                for i in range(n-2, 0, -1):
                    yield i, 0
        offset = 0
        num = 1
        for idx in range(n, 0, -2):
            for r,c in getidx(idx):
                res[offset + r][offset + c] = num
                num += 1
            offset += 1
        return res

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        if n==0:
            return []
        direction='right'
        top=0
        bottom=n-1
        right=n-1
        left=0
        result=[[0 for i in range(n)] for i in range(n)]
        counter=1
        while left<=right and top<=bottom:
            if direction=='right':
                for i in range(left,right+1):                   
                    result[top][i]=counter
                    counter+=1
                direction='bottom'
                top+=1
            elif direction =='bottom':
                for i in range(top,bottom+1):                   
                    result[i][right]=counter   
                    counter+=1
                right-=1
                direction='left'
                
            elif direction=='left':
                
                for i in range(right,left-1,-1):   
                    
                    result[bottom][i]=counter
                    counter+=1
                bottom-=1
                direction='top'
            elif direction=='top':
                for i in range(bottom,top-1,-1):                   
                    result[i][left]=counter
                    counter+=1
                left+=1
                direction='right'
        return result        

# 일단 값넣고
# 끝에 도착하거나, 숫자가 존재하면 방향 전환!
# for 마지막에 next 방향 정해줌!
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[None] * n for _ in range(n)]
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # increment x, increment y
        
        pos = [0, 0]
        cur = 0
        for i in range(1, n*n+1):
            arr[pos[0]][pos[1]] = i
            
            new_pos = [pos[0] + move[cur][1], pos[1] + move[cur][0]]
            if new_pos[0] < 0 or new_pos[0] >= n or \
                new_pos[1] < 0 or new_pos[1] >= n or \
                    arr[new_pos[0]][new_pos[1]]:
                cur += 1
                if cur > 3:
                    cur = 0

            pos[0] += move[cur][1]
            pos[1] += move[cur][0]
        return arr

# 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ele = 1
        mat = [[0]*n for _ in range(n)]
        # print(mat)
        sr = sc = 0
        er = ec = n-1
        while sr <= er and sc <= ec:
            for i in range(sc,ec+1):
                mat[sr][i] = ele
                ele += 1
            for i in range(sr+1,er+1):
                mat[i][ec] = ele
                ele += 1
            for i in reversed(range(sc,ec)):
                mat[er][i] = ele
                ele += 1
            for i in reversed(range(sr+1,er)):
                mat[i][sc] = ele
                ele +=1
            sr += 1
            sc += 1
            er -= 1
            ec -= 1
        return mat

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return self.generateMatrixb(n, 0, 0, 0, [ [0]*n for _ in range(n) ], 1)
    
    def generateMatrixb(self, n, r, c, direc, matrix, num):
        if r < 0 or r == n or c < 0 or c == n or matrix[r][c] != 0:
            return matrix
        
        matrix[r][c] = num
        
        EAST = 0
        SOUTH = 1
        WEST = 2
        NORTH = 3
        
        vR = r
        vC = c
        
        if direc == EAST:
            vC += 1
        elif direc == SOUTH:
            vR += 1
        elif direc == WEST:
            vC -= 1
        else:
            vR -= 1
        
        if vR < 0 or vC < 0 or vR == n or vC == n or matrix[vR][vC] != 0:
            direc = (direc + 1) % 4
            if direc == EAST:
                c += 1
            elif direc == SOUTH:
                r += 1
            elif direc == WEST:
                c -= 1
            else:
                r -= 1
        else:
            r = vR
            c = vC
        
        return self.generateMatrixb(n, r, c, direc, matrix, num + 1)