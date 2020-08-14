# problem : 전화번호 목록

 def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda x : len(x) )
    for i in range(len(phone_book)):
        small = phone_book[i]
        for j in range(i+1, len(phone_book)):
            large = phone_book[j]
            if small == large[:len(small)]:
                return False
    return True

"""
# sorting 을 이용하여 각각의 앞뒤만 비교
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
"""