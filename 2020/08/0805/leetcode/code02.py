# Valid Palindrome

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=re.split('[^a-zA-Z0-9]',s.lower())
        print(a)
        new_s = "".join(a)
        start = 0
        end = len(new_s)-1
        if len(new_s) == 1:
            return True
        while True:
            if start > end:
                break
            if new_s[start] != new_s[end]:
                return False
            start +=1
            end -= 1

        return True
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed

# ^x 문자열의 시작을 표현하며 x 문자로 시작됨을 의미한다.
# x$ 문자열의 종료를 표현하며 x 문자로 종료됨을 의미한다.
# [^xy] not 을 표현하며  x 및 y 를 제외한 문자를 의미한다


# arr[::-1] 은 reverse 임.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub(r'[^\w]','',s) 
#         s = s.replace('_','')
#         return s == s[::-1]

# reverse 해서 확인하자!
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         return (lambda x:x == x[::-1])([c for c in s.lower() if c.isalnum()])