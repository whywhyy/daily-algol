# Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()

        check = set()
        if len(s) <10:
            return []

        for i in range(len(s)-9):
            now = s[i:i+10]
            if now in check:
                result.add(now)
            check.add(now)

        
        return list(result)

# # default dict 대신 dict.get(key,val) 로 정의!
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
#         ans = []
#         count = {}
        
#         for i in range(10, len(s) + 1):
#             sub_str = s[i-10: i]
#             count[sub_str] = count.get(sub_str, 0) + 1
#             if count[sub_str] == 2:
#                 ans.append(sub_str)
#         return ans

# 나의 풀이와 동일
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L=10
        n = len(s)
        seen = set()
        output = set()
        for i in range(n-L+1):
            tmp = s[i:i+L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output

# 2 일때만 ans 에 append! 
# 가장 좋은 방법인듯함 아마!? 갯수를 샐수 있어서!?
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        if len(s) == 10:
            return []
        d = {}
        ans = []
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key in d:
                d[key] += 1
                if d[key] == 2:
                    ans.append(key)
            else:
                d[key] = 1
        return ans


# 풀이 동일!
# 다만 if else 로 처리 seen에 존재하면 new 에 추가!
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen = set()
        res = set()
        for i in range(len(s)):
            new = s[i: i+10]
            if new in seen:
                res.add(new)
            else:
                seen.add(new)
        return res