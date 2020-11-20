# Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            ston = i
            if not stack:
                stack.append(ston)
            else:
                if stack[-1] >0 and ston > 0:
                    stack.append(ston)
                    continue
                if stack[-1] <0:
                    stack.append(ston)
                    continue
                # +-
                while stack and stack[-1]>0 and ston < 0:
                    if abs(ston) < stack[-1]:
                        break
                    if abs(ston) == stack[-1]:
                        stack.pop()
                        break
                    if abs(ston) > stack[-1]:
                        stack.pop()                
                        if not stack or stack[-1] <0 :
                            stack.append(ston)
                            break
        return stack

# 깔끔하지만 while else , for else 가 존재한다 !!
# while else 의 경우 while 이 실패시 else 동작
# for else 의 경우 for 정상 동작시 else 동작
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                if not stack or stack[-1]<0:
                    stack.append(a)
                else:
                    while stack:
                        if stack[-1]+a == 0:
                            stack.pop()
                            break
                        if stack[-1]+a>0:
                            break
                        if stack[-1] > 0:
                            stack.pop()
                        else:
                            stack.append(a)
                            break
                    else:
                        stack.append(a)
        return stack

# 최소한 하나의 astroid 는 남으므로 !
# 
class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while asteroid < 0 and stack and stack[-1] > 0:
                temp = stack.pop()
                if temp + asteroid > 0:
                    asteroid = temp
                elif temp + asteroid == 0:
                    asteroid = 0
            
            if asteroid:  # valid asteroid after all collisions
                stack.append(asteroid)
        
        return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        '''
        Collisions 
        -> <-
        Iterate        
        '''
        
        
        stack = []

        for asteroid in asteroids:
            appendAsteroid = True
            while stack and asteroid < 0 < stack[-1]:
                # If incoming asteroid weighs more 
                if abs(asteroid) > stack [-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                appendAsteroid = False
                break
            if appendAsteroid:
                stack.append(asteroid)
        
        return stack
#
# 오른쪽으로 가다가 터트릴애들은 다 터트린다!? 늦게들어온 오른쪽은 남긴다!
# 왼쪽으로 가다가 터트릴 애들은 다 터트린다 !? 앞쪽의 왼쪽은 남긴다!
from queue import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stackleft=deque()
        stackright=deque()
        
        for asteroid in asteroids:
            if asteroid>0: 
                stackright.append(asteroid)
            else:
                while stackright and stackright[-1]<=abs(asteroid):
                    temp=stackright[-1]
                    stackright.pop()
                    if temp==abs(asteroid):break
            
        for asteroid in reversed(asteroids):
            if asteroid <0:
                stackleft.appendleft(asteroid)
            else:
                while stackleft and abs(stackleft[0])<=asteroid:
                    temp=stackleft[0]
                    stackleft.popleft()
                    if abs(temp)==asteroid:break
        return stackleft+stackright