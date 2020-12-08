# Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # max flower !?
        dp = [0] * len(flowerbed)
        
        if n is 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True

        if flowerbed[0] == 1 or flowerbed[1] == 1:
            dp[0] = 0
            dp[1] = 0
        else:
            dp[0] = 1
            dp[1] = 1

        for i in range(2, len(flowerbed)-1):
            before = flowerbed[i-1]
            now = flowerbed[i]
            after = flowerbed[i+1]

            if now == 0:
                if before == 0 and after == 0:
                    dp[i] = max(dp[i-1], dp[i-2] + 1)
                else:
                    dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], dp[i-2])
        
        if len(flowerbed) > 2:
            if flowerbed[-1] == 1 or flowerbed[-2] == 1:
                dp[-1] = max(dp[-2], dp[-3])
            else:
                dp[-1] = max(dp[-2], dp[-3]+1)


        return True if n <= dp[-1] else False

# 꽃을 심을수 있는 자리라면 바로 꽃심기 !
# i ==0 인경우 : 현재자리가 0, flowerbed[i + 1] == 0, 이후 flowerbed[i] = 1 !!
# i != 0 인경우 : 현재자리가 0, flowerbed[i - 1] == 0, 마지막 꽃 or flowerbed[i + 1] == 0)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i= 0
        count= 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and ( i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n

# 앞뒤로 0 을 심는다 !!
# if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0: 이면
# n-=1  flowerbed[i] = 1   로 구현 !
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        size = len(flowerbed)
        flowerbed = [0]+flowerbed+[0]
        for i in range(1, size+1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                n-=1
                flowerbed[i] = 1   
                if n == 0: return True
        return False

# 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n > len(flowerbed):
            return False
        
        if n == 0:
            return True
        
        if not flowerbed:
            return n == 0

        # n = 2, 0 0 1
        # n = 0, 0 0 0
        # n = 2, 0 0 0 0 0 1 0 1 0 1
        
        # 0 0 0 0 0 0
        # x 0 0 0 0 x
        
        if flowerbed[0] == 0:
            if len(flowerbed) == 1 or flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        
        if flowerbed[-1] == 0:
            if len(flowerbed) == 1 or flowerbed[len(flowerbed)-1-1] == 0:
                flowerbed[-1] = 1
                n -= 1
        
        return n <= 0

# 위와 동일
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if not flowerbed:
            return n == 0
        
        for i, bed in enumerate(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0

# 연속으로 0 3번이면 count +=1 
# 그 후 count = 1 로 설정 count 3 중에 중앙에 꽃을 심었기때문에
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0,0)
        count = 0
        for bed in flowerbed:
            if bed == 0:
                count += 1
            else: 
                count = 0
            if count == 3:
                n -= 1
                count = 1
        if n <= 0:
            return True
        return False

# 위와 동일 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0] #modifies input
        for i in range(1, len(flowerbed)-1):
        	if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        		flowerbed[i] = 1
        		count += 1
        return count >= n

# 위와 동일 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
                
        if count >= n:
            return True
        else:
            return False