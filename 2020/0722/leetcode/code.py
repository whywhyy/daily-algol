# problem : Word Search


import copy
class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j] :
                    index = 0
                    check = [[False for x in range(len(board[i]))] for y in range(len(board))] 
                    check[i][j] = True
                    stack.append((i,j,check,index)) # now, check, index 
        while len(stack):
            now_x,now_y,check_board,word_index = stack.pop()
            if word_index == len(word)-1:
                return True
            # left
            if now_y != 0 and check_board[now_x][now_y-1] == False:
                if board[now_x][now_y-1] == word[word_index+1]:
                    new_check = copy.deepcopy(check_board)
                    new_check[now_x][now_y-1] = True
                    stack.append((now_x,now_y-1,new_check,word_index+1)) # now, check, word_index 
            # right
            if now_y != len(board[0])-1 and check_board[now_x][now_y+1] == False:
                if board[now_x][now_y+1] == word[word_index+1]:
                    new_check = copy.deepcopy(check_board)
                    new_check[now_x][now_y+1] = True
                    stack.append((now_x,now_y+1,new_check,word_index+1)) # now, check, word_index 
            # up
            if now_x != 0 and check_board[now_x-1][now_y] == False:
                if board[now_x-1][now_y] == word[word_index+1]:
                    new_check = copy.deepcopy(check_board)
                    new_check[now_x-1][now_y] = True
                    stack.append((now_x-1,now_y,new_check,word_index+1)) # now, check, word_index 
            # down
            if now_x != len(board)-1 and check_board[now_x+1][now_y] == False:
                if board[now_x+1][now_y] == word[word_index+1]:
                    new_check = copy.deepcopy(check_board)
                    new_check[now_x+1][now_y] = True
                    stack.append((now_x+1,now_y,new_check,word_index+1)) # now, check, index        
        return False

"""
 dfs 로 풀었는데, Runtime 도 길고, Memory Usage 도 컸다.
 얕은 복사 때문에 문제가 되서 깊은 복사로 문제를 풀었다.
"""

"""
# 상수로 board lenX, lenY, lenW 를 설정.
# def 안에 def 로 dfs 를 정의하였음.
# dfs(x,y,idx) 는 x,y check 해야할 현재 위치. 
# 재귀적으로 동작 dfs 에서 def(x-1,y,idx) 형식으로 동작.
# 하나라도 True 라면 True 반환.
# if dfs(x-1, y, idx) or dfs(x, y-1, idx) or dfs(x+1, y, idx) or dfs(x, y+1, idx):
#         return True
# tmp 를 사용하여 board 의 상태를 회복시킴!

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenX, lenY = len(board), len(board[0])
        lenW = len(word)

        def dfs(x, y, idx):
            if idx == lenW:
                return True
            if (x < 0 or x >= lenX) or (y < 0 or y >= lenY) or board[x][y] != word[idx]:
                return False

            tmp = board[x][y]
            board[x][y] = "#"
            idx += 1

            if dfs(x-1, y, idx) or dfs(x, y-1, idx) or dfs(x+1, y, idx) or dfs(x, y+1, idx):
                # board[x][y] = tmp
                return True
            else:
                board[x][y] = tmp
                return False

        for i in range(lenX):
            for j in range(lenY):
                if dfs(i, j, 0):
                    return True
        return False
"""


        

