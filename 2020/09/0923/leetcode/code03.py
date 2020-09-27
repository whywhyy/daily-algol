# Robot Bounded In Circle
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0,0]
        pos = 'R'
        instructions = instructions * 4
        # default Y +
        # R -> LR
        # U -> LR
        # D -> LR
        # L -> LR
        for i in instructions:
            x, y = start
            if i == 'G':
                if pos == 'R':
                    start = [x, y+1]
                elif pos == 'U':
                    start = [x-1, y]
                elif pos == 'D':
                    start = [x+1, y]
                elif pos == 'L':
                    start = [x, y-1]
            elif i == 'L':
                if pos == 'R':
                    pos = 'U'
                elif pos == 'U':
                    pos = 'L'
                elif pos == 'D':
                    pos = 'R'
                elif pos == 'L':
                    pos = 'D'
            elif i == 'R':
                if pos == 'R':
                    pos = 'D'
                elif pos == 'U':
                    pos = 'R'
                elif pos == 'D':
                    pos = 'L'
                elif pos == 'L':
                    pos = 'U'             
        if start == [0,0]:
            return True
        else:
            return False

# # 처음 진행 방향만 아니여도 accepted 줌 !
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         x, y = 0, 0
#         d = 0
        
#         for i in instructions:
#             if i == 'G':
#                 x += directions[d%4][0]
#                 y += directions[d%4][1]
#             elif i == 'L':
#                 d -= 1
#             else:
#                 d += 1
        
#         return (x, y) == (0, 0) or d%4 != 0

# # ㄹㅇ 각도로 접근
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         direction = 90
#         position = [0, 0]
        
#         for i in instructions:
#             if i == "G":
#                 if direction == 0:
#                     position[0] += 1
#                 elif direction == 90:
#                     position[1] += 1
#                 elif direction == 180:
#                     position[0] -= 1
#                 elif direction == 270:
#                     position[1] -= 1
#             if i == "R":
#                 direction = (direction - 90)
#                 if direction < 0:
#                     direction = direction + 360
#             if i == "L":
#                 direction = (direction + 90) % 360
                
        
#         if position[0] == 0 and position[1] == 0:
#             return True

# # 개신기 하넹
# # -1 % 4 => 3 나옴!  === 5 % 4 와 동일! 
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         pos = (0, 0)
#         rot = 0
#         for instruction in instructions:
#             if instruction == 'L':
#                 rot = (rot - 1) % 4
#             elif instruction == 'R':
#                 rot = (rot + 1) % 4
#             else: #instruction == 'G':
#                 if rot == 0:
#                     pos = (pos[0], pos[1] + 1)
#                 elif rot == 1:
#                     pos = (pos[0] + 1, pos[1])
#                 elif rot == 2:
#                     pos = (pos[0], pos[1] - 1)
#                 else: #rot == 3
#                     pos = (pos[0] - 1, pos[1])
        
#         return pos == (0, 0) or rot != 0
            
# # # 대박
# #             elif ins == "L": 
# #                 di, dj = dj, -di
# #             elif ins == "R": 
# #                 di, dj = -dj, di
# # 이게 맞네!
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         i = j = 0
#         di, dj = 0, 1
#         for ins in instructions:
#             if ins == "G":
#                 i += di
#                 j += dj
#             elif ins == "L": 
#                 di, dj = dj, -di
#             elif ins == "R": 
#                 di, dj = -dj, di
#         return (i, j) == (0, 0) or (di, dj) != (0, 1)