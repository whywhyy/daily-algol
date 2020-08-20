# Goat Latin

class Solution:
    def toGoatLatin(self, S: str) -> str:
        arr = S.split()
        for i in range(len(arr)):
            now = arr[i]
            now = now.lower()
            if now[0] == 'a' or now[0] == 'e' \
                or now[0] == 'i' or now[0] == 'o' \
                    or now[0] == 'u':
                arr[i] += 'ma'
            else:
                arr[i] = arr[i][1:] + arr[i][0] + 'ma'
            arr[i] += 'a'*(i+1)

        return " ".join(arr)

# # 
# 풀때마다 느끼지만
# 어떤 자료형을 써야겠다. 단순 풀이 알고리즘에만 적용하려고 한다.
# 단순 문제풀이 뿐만 아니라 과정속에도 자료형을 쓰는 습관을 들여야 겠다.
# 아래는 set 을 이용했다.
# 그리고 직접 데이터 자체를 건드려서 수정했는데.
# 새로 만들어서 res.append 하는 습관을 들여야 겠따. 
#
# class Solution:
#     def toGoatLatin(self, S: str) -> str:
#         words = S.split(' ')
#         if not words:
#             return ''
#         res = []
#         vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
#         for i, word in enumerate(words):
#             if word[0] in vowels:
#                 res.append(word+'ma'+'a'*(i+1))
#             else:
#                 res.append(word[1:]+word[0]+'ma'+'a'*(i+1))
#         return ' '.join(res)