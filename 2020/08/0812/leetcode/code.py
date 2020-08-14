# Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        result.append([1])
        result.append([1,1])
        for i in range(32):
            result.append([])
            result[-1].append(1)
            for j in range(len(result[-2])-1):
                result[-1].append(result[-2][j] + result[-2][j+1])
            result[-1].append(1)
        return result[rowIndex]


# #
# 어차피(?) row 의 수는 정해져 있으니 row 에 확정된 list 의 길이를 넣는다!.
# triangle 이라는 멋진 변수명을 썼다!(?)
# 확실히 append 를 여러번 하는것보다.
# 선언해서 놓고 데이터를 넣는게 빠르다.
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         triangle = []
#         for row_num in range(rowIndex + 1):
#             row = [None]*(row_num + 1)
#             row[0] = 1
#             row[-1] = 1
#             for j in range(1, row_num):
#                 row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#             triangle.append(row)
#         return row