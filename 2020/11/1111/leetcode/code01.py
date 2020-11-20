# Flipping an Image

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # reverse
        for i in range(len(A)):
            A[i] = A[i][::-1]

        # invert 
        A = [[ 0 if A[i][j]==1 else 1 for j in range(len(A[i]))   ]
                for i in range(len(A))] 
        
        return A

# row reverse 이후 xor 연산 !!
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for i in range(len(row)):
                row[i] ^= 1
        return A

# for x in reversed(row): 로 진행 !  int(not x) 로 변경 !!
# not 1 => 0 ,  not 0 => 1
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for row in A:
            new_row = []
            result.append(new_row)
            for x in reversed(row):
                new_row.append(int(not x))
        return result

# simple !
# if 문이 생각보다 빠르다!?
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for i in range(len(A)): 
            A[i].reverse()
            for j in range(len(A[i])): 
                if A[i][j] == 0: 
                    A[i][j] = 1
                else: 
                    A[i][j] = 0
        return A

# 음.. 이건 왜 맞지?
# not 0 -> -1 ?? 맞네 왜!?
# x => ~(x - 1) = -x  임 ! 
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        B = [[] * len(A)]
        for row in A:
            for j in range((len(row) + 1) // 2):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1
        
        return A

# 아 !
# ADD !!
# row[-j-1], row[j] = row[j]^1 , row[-j-1] ^ 1
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for row in A:
            for j in range((len(row) + 1) // 2):
                row[j], row[-j-1] = row[-j-1] ^ 1, row[j] ^ 1
        
        return A