# Mirror Reflection
import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        p, q = p//math.gcd(p,q), q//math.gcd(p,q)
        if p % 2 == 0:
            # 2,3
            if q %2 == 0:
                return 3
            else:
                return 2
        else:
            # 1,0
            if q%2 ==0:
                return 0
            else:
                return 1


            return 1

# 오홓 알고보면(!?) 알겠따..
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while (p % 2 == 0 and q % 2 == 0):
            p //= 2
            q //= 2
        if p % 2 == 0: return 2   # if p%2==0 && q%2==0 then q originally != 0, or p%2=1 at end
        if q % 2 == 0: return 0
        return 1



class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        m, n = q // g, p // g
        if n % 2 == 0:
            return 2
        else:
            return m % 2
        return -1

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)
        
        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0