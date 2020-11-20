# 1625. Lexicographically Smallest String After Applying Operations
# BFS # 1292 ms
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result = s
        check = set()
    
        queue = []
        queue.append(s)
        while queue:
            
            now = queue.pop()
            if now not in check:
                check.add(now)
                result = sorted([now,result])[0]
                # a
                # print(now[-b:]+now[:-b])
                queue.append(now[-b:]+now[:-b])
                # b
                # print(self.add_digit(now, a))
                queue.append(self.add_digit(now, a))
        return result
        
    def add_digit(self, ist_str, ist_b):
        new = list(ist_str)
        for i in range(len(ist_str)//2):
            now = ist_str[i*2-1]
            now_i = (int(now) + ist_b) % 10
            # print(now, type(str(now)))
            new[i*2-1] = str(now_i)
        
        return "".join(new)

# # DFS
# class Solution:
#     def findLexSmallestString(self, s: str, a: int, b: int) -> str:
#         nums = tuple(map(int, s))
#         N = len(nums)
#         self.res = nums
#         v = set()

#         def dfs(cur):
#             if cur not in v:
#                 v.add(cur)
#                 if cur < self.res:
#                     self.res = cur
#                 # Operation 1
#                 l = list(cur)
#                 for i in range(1, N, 2):
#                     l[i] = (l[i] + a) % 10
#                 dfs(tuple(l))
                
#                 # Operation 2
#                 l = list(cur)
#                 num = N - b
#                 dfs(tuple(l[-num:] + l[:-num]))
        
#         dfs(nums)
#         return ''.join(str(i) for i in self.res)

# # 문자의 길이, b 와의 최대 공약수를 구함
# # -> Nr 최대 공약수 만큼 회전하면 처음과 동일한 문자임!
# # 
# # 10 과 a 의 최대공약수를 구함
# # -> Nd 
# # 
# # if Nr%2:  이유 ->  
# class Solution:
#     def findLexSmallestString(self, s: str, a: int, b: int) -> str:
#         N = len(s)
#         if N == 1: 
#             return ''
#         Nr = math.gcd(N, b)
#         Nd = math.gcd(10, a)
#         mins = ''
#         for start in range(0, N, Nr): 
#             istart = int(s[start])
#             inext = int(s[(start+1)%N])
            
#             sevenprev = istart
#             soddprev = inext
#             if Nr%2: 
#                 strbuilder = [sevenprev % Nd, soddprev % Nd]
#             else: 
#                 strbuilder = [sevenprev, soddprev % Nd]
#             for i in range(1, N//2): 
#                 ie = (start + 2*i)%N
#                 io = (start + 2*i+1)%N
#                 seven = int(s[ie])
#                 sodd = int(s[io])
#                 if Nr%2: 
#                     strbuilder.append((strbuilder[-2] + seven - sevenprev) % 10)
#                 else: 
#                     strbuilder.append(seven)
#                 soddn = (strbuilder[-2] + sodd - soddprev) % 10
#                 strbuilder.append(soddn)
#                 sevenprev = seven
#                 soddprev = sodd
#             curs = ''.join(map(str, strbuilder))
#             if not mins or curs<mins: 
#                 mins = curs
#         return mins
            
# # to_ret -> 회전없이 ADD 의 모든수
# # 
# class Solution:
#     def findLexSmallestString(self, s: str, a: int, b: int) -> str:
#         it2st = lambda x : ''.join([str(t) for t in x])
#         st2it = lambda x : [int(c) for c in x]
        
#         to_ret = [s]
#         sint = st2it(s)
#         for _ in range(9) :
#             for i in range(1, len(s), 2) :
#                 sint[i] = (sint[i] + a) % 10
#             to_ret.append(it2st(sint))
#         to_ret = list(set(to_ret))
        
#         to_ret_new = [t for t in to_ret]
#         if b % 2 == 1 :
#             for st in to_ret :
#                 sint = st2it(st)
#                 for _ in range(9) :
#                     for i in range(0, len(s), 2) :
#                         sint[i] = (sint[i] + a) % 10
#                     to_ret_new.append(it2st(sint))
#             to_ret = list(set(to_ret_new))
        
#         to_ret_new = [t for t in to_ret]
#         for st in to_ret :
#             sint = st
#             for _ in range(len(s)) :
#                 st = st[-b:] + st[:-b]
#                 to_ret_new.append(st)
#         to_ret = list(set(to_ret_new))
#         return min(to_ret)