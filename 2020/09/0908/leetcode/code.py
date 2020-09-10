# Word Pattern

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        check_pattern = defaultdict(type(""))
        check_use= defaultdict(type(""))
        now_str = str.split()
        if len(pattern) != len(now_str):
            return False
        for i in range(len(now_str)):
            if pattern[i] in check_use or now_str[i] in check_pattern:
                if check_use[pattern[i]] != now_str[i] or check_pattern[now_str[i]] != pattern[i]:
                    return False
            else:
                check_use[pattern[i]] = now_str[i]
                check_pattern[now_str[i]] = pattern[i]

        return True

# # awesome
# # 쩐다 ! 
# """
# # lsp== len(set(zip(pattern, x)))
# "aba"
# "dog cat cat"
# """
# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         x = str.split(' ')
#         lsp = len(set(pattern))
#         lsx = len(set(x))
#         return len(x)==len(pattern) and lsx==lsp and lsp== len(set(zip(pattern, x)))


# # zip 으로 묶어서 for in 동작 !
# # word_to_letter
# # letter_to_word 로 잘 나누어서 구현했다.
# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         words = str.lstrip().split(" ")
        
#         if len(words) != len(pattern):
#             return False
        
#         letter_to_word = {}
#         word_to_letter = {}
        
#         for letter, word in zip(pattern, words):
#             if not letter in letter_to_word:
#                 letter_to_word[letter] = word
#             elif letter_to_word[letter] != word:
#                 return False
            
#             if not word in word_to_letter:
#                 word_to_letter[word] = letter
#             elif word_to_letter[word] != letter:
#                 return False
            
#         return True