# Minimum Cost to Move Chips to The Same Position

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        if odd == 0 or even == 0:
            return 0
        else:
            return min(odd,even)

# 갯수로 접근 !
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum([pos % 2 for pos in position])
        return min(odd, len(position) - odd)

# 그냥 둘중하나 최소값!
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        d = {}
        a = 0
        b = 0
        for i in position:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if i%2==0:
                a +=d[i]
            else:
                b+=d[i]
        return min(a,b)