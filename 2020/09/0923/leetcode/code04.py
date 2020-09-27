# Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():
            return 0
        return  len(s.split()[-1])

# # 쫌더 깔끔쓰
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         x = s.split()
#         if len(x) > 0:
#             return len(x[-1])
#         return 0
        