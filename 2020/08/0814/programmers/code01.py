# leetcode 에서 풀었던거라 스킵
# h index
def solution(citations):
    citation = len(citations)
    citations = sorted(citations, reverse=True)
    # 100 90 11 20
    for idx,val in enumerate(citations):
        if citations[citation-1] >= citation:
            return citation
        else :
            citation -=1

    return citation