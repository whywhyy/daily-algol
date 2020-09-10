# Bulls and Cows
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        secret = list(secret)
        guess = list(guess)
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                secret[i] = '*'
                guess[i] = '*'
                A += 1
        
        for i in range(len(guess)):
            if guess[i] != '*':
                if guess[i] in secret:
                    B+=1
                    secret[secret.index(guess[i])] = '*'

        return str(A)+"A"+str(B)+"B"

# # Counter 활용 !
# # awesome
# # counter 에 존재하면 A 인지 B 인지 확인!
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:        
#         counter = Counter(secret)
        
#         bulls = cows = 0
#         for i, ch in enumerate(guess):
#             if ch in counter:
#                 if ch == secret[i]:
#                     bulls += 1
#                     cows -= int(counter[ch] <= 0)
#                 else:
#                     cows += int(counter[ch] > 0)
                
#                 counter[ch] -= 1
            
#         return f"{bulls}A{cows}B"

# # awesome
# # array 길이가 같은 경우 zip 을 활용하자!
# # Counter 로 잘 처리했다 c 를 정의하는 부분이 좋은 접근같다.
# # c+=min(d1[i],d2[i]) /  "{}A{}B".format(b,c-b) 
# # c+=min(d1[i],d2[i]) 전체 무조건 B 로 처리하는경우임
# # 즉 모든 B 에서 A 를 빼주면 된다 ! "{}A{}B".format(b,c-b) 
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         c,b=0,0
#         for i in zip(secret,guess):
#             if i[0]==i[1]:
#                 b+=1
#         d1=Counter(secret)
#         d2=Counter(guess)
#         for i in d1:
#             if i in d2:
#                 c+=min(d1[i],d2[i])
#         return "{}A{}B".format(b,c-b)

# # 신박 ! 
# # awesome 
# # dict로 counter[s] += 1, counter[g] -= 1 로 guess가 있는지 secret 이 있는지 체크!
# # counter[s] < 0 이면 이전 guess 가 있었으니 cow += 1
# # counter[g] > 0 이면 이전 secret 이 있었으니 cow += 1
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bulls, cows = 0, 0
#         counter = collections.defaultdict(int)

#         for idx in range(len(secret)):
#             s = secret[idx]
#             g = guess[idx]
#             if s == g:
#                 bulls += 1
#             else:
#                 if counter[s] < 0:
#                     cows += 1
#                 if counter[g] > 0:
#                     cows += 1
#                 counter[s] += 1
#                 counter[g] -= 1
#         return f"{bulls}A{cows}B"


# # # 
# # awesome
# #         for c in set(secret):
# #             cows += min(secret.count(c), guess.count(c))
# # cow += min(secret.count(c), guess.cont(c))
# # 모든 cow 것 을 cow 로 계산하는 방법. 실제 cow 는 cow - bull 임 ! 
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
        
#         bull=0
#         for i in range(len(secret)):
#             bull += int(secret[i] == guess[i])
        
# 		# This loop will take care of "cow" cases
#         cows=0
#         for c in set(secret):
#             cows += min(secret.count(c), guess.count(c))
        
#         return f"{bull}A{cows-bull}B"