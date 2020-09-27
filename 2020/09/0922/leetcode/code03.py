# Sequential Digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        l_len = len(str(low))
        h_len = len(str(high))

        for i in range(l_len, h_len+1):
            for j in range(1, 10-i+1):
                now = str(j)
                for k in range(i-1):
                    now += str(int(now[-1])+1)
                    if now[-1] == '9':
                        break
                if len(now) == i and low<=int(now)<=high:
                    result.append(int(now))

        return result

# # deque 1~9 를 넣고
# # 1 빼고 12 를 맨뒤에 다 시 넣기 !
# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         out = []
#         queue = deque(range(1,10))
#         while queue:
#             elem = queue.popleft()
#             if low <= elem <= high:
#                 out.append(elem)
#             last = elem % 10
#             if last < 9: 
#                 queue.append(elem*10 + last + 1)                
#         return out

# # 1 로 시작 1 12 123 try~
# # 2 로 시작 2 23 456
# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         res=[]
#         for digit in range(1,10):
#             num=nxt=digit
#             while num<=high and nxt<10:
#                 if num>=low:
#                     res.append(num)
#                 nxt+=1
#                 num=num*10+nxt   
#         return sorted(res)


# # "123456789" 를 만들어 놓고 짜르자!
# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         s = "123456789"
#         def f(d, start, end) -> []:
#             idx = d
#             out = []
#             while idx <= len(s):
#                 c = int(s[idx-d:idx])
#                 if c >= start:
#                     if c <= end:
#                         out.append(c)
#                     else: break
#                 idx += 1
#             return out
        
#         out = []
#         for l in range(len(str(low)), len(str(high))+1):
#             out.extend(f(l, low, high))
#         return out

# # queue 를 이용하여 확인하고 뒤에 넣기 ! 
# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         ret = []
#         queue = list(range(1,10))
#         while len(queue) > 0:
#             val = queue.pop(0)
#             if val >= low and val <= high:
#                 ret.append(val)
#             elif val > high:
#                 continue
#             last = int(str(val)[-1])
#             if last == 9: continue
#             temp = str(val) + str(last + 1)
#             queue.append(int(temp))
#         return sorted(ret)