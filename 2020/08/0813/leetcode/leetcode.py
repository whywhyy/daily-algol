#  Iterator for Combination

from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.result = list(combinations([x for x in characters], combinationLength))
        self.count = 0

    def next(self) -> str:
        return_val = "".join(self.result[self.count]) 
        self.count += 1
        return return_val
        
    def hasNext(self) -> bool:
        if self.count <= len(self.result)-1:
            return True
        return False

# 조합의 특징을 잘 알고
# For문을 잘 돌렸다 (?)
# while 안에서 returns 을 동작시켜 yield 는 아닌데 맞는듯한(?) 느낌을 받았다.
# class CombinationIterator:
#     def __init__(self, characters: str, combinationLength: int):
#         self.length = combinationLength
#         self.chars = characters
#         self.indexes = {self.chars[i]:i for i in range(len(self.chars))}
#         self.q = deque([[x] for x in self.chars])
                
#     def next(self) -> str():
#         curr = []
#         while self.q:
#             curr = self.q.popleft()
#             if len(curr) == self.length:
#                 return "".join(curr) 
#             for j in range(self.indexes[curr[-1]]+1, len(self.chars)):
#                 self.q.append(curr + [self.chars[j]])
#         return ""
        
#     def hasNext(self) -> bool:
#         return bool(self.q)

# awesome !.
# 어메이징 하다. 잘 이해가 안되서 combinationLength = 1 일때 부터 어떻게 동작할지
# 생각해 봤다.
# 역시 조합의 특징상
# N개 일때 len(char) - N +1 로 처리한다. (필요없는 시작부분 제거)
# characters[i+1:] 분도 잘 고려한것 같다.
# 
# class CombinationIterator:
#     def __init__(self, characters: str, combinationLength: int):
#         self.generator = self.df(characters, combinationLength, '')
#         self.nxtCom = None
#         self.nextCalled = True

#     def next(self) -> str:
#         if self.hasNext():
#             self.nextCalled = True
#             return self.nxtCom

#     def hasNext(self) -> bool:
#         if self.nextCalled:
#             self.nextCalled = False
#             self.nxtCom = next(self.generator, False)
#         return bool(self.nxtCom)
        
#     def df(self, characters:str,  combinationLength:int, path:str):
#         if combinationLength == 0:
#             yield path
#         else:
#             for i, ch in enumerate(characters[:len(characters)-combinationLength+1]):
#                 yield from self.df(characters[i+1:], combinationLength-1, path+ch)