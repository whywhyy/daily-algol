# Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        now = 0
        for i in str(num): 
            now += int(i)
            if now % 10 == 0:
                now //=10
        
        while len(str(now)) >= 2:
            result = 0
            for i in str(now):
                result += int(i)
            if result % 10 == 0:
                result //= 10
            now = result
        return now

"""
# 응!? O(1) !!?!?
# https://en.wikipedia.org/wiki/Digital_root
# 그러니까 base 10, 3110 -> 3,1,1,0
# base 3 , 20 -> (9->2 3->2)  -> 4 -> 1 인가!?
# 그래서 결론은  
# 0 == 0
# ((n-1) mod (b-1)) + 1 이군
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        else: 
            return (num-1) %9 +1
"""