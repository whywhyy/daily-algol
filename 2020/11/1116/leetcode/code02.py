# Poor Pigs
# 
import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # bucket, Die time, Test TIME!
        period = minutesToTest // minutesToDie + 1
        # period ** (pigs-1) >= bucket 
        
        return math.ceil(math.log(buckets,period))
        # for i in range(buckets):
        #     if period **(i) >= buckets:
        #         return i
    
# log 를 사용하다니 awesome 하다! 