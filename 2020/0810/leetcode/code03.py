# H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation = len(citations)
        citations = sorted(citations, reverse=True)
        # 100 90 11 20
        for idx,val in enumerate(citations):
            if citations[citation-1] >= citation:
                return citation
            else :
                citation -=1
            
        return citation


# 어차피 len(citations) 이니까
# 그냥 for 에 N번 돈다!
# 
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         n = len(citations)
#         for i in range(n):
#             if citations[i] >= n - i:
#                 return n-i
#         return 0