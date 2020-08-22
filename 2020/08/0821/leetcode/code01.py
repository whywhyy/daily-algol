# Sort Array By Parity

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        for i in A:
            if i % 2 ==0:
                result.insert(0,i)
            else:
                result.append(i)
        return result

# Sort Array By Parity
from collections import deque

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = deque()
        for i in A:
            if i % 2 ==0:
                result.appendleft(i)
            else:
                result.append(i)
        return result

# awesome 하다.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]


# sorting 으로도 가능하다! awesome X 100 ;;
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x%2)
        return A