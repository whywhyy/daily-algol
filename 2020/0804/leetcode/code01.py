# Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) ==1 :
                return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
        if word.islower():
            return True
        return False

# # title 이라는 string method 가 존재한다!
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         if word.lower() == word: return True
#         elif word.upper() == word: return True
#         elif word.istitle(): return True
#         else: return False