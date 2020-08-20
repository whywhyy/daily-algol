# Numbers With Same Consecutive Differences

# start 1 .. -> start candi -> start candi
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]

        queue = []
        for i in range(1,10):
            queue.append((str(i), 1))
        
        result = []
        while queue:
            now_str, now_len = queue.pop()
            if len(str(int(now_str))) == N:
                result.append(int(now_str))
                continue
            else:
                if now_len == N:
                    continue
            
            last_now = now_str[-1]
            last_arr = []
            
            try_last = int(last_now)
            if K == 0:
                last_arr.append(str(try_last))
            else:
                if try_last-K >= 0:
                    last_arr.append(str(try_last-K))
                if try_last+K <= 9:
                    last_arr.append(str(try_last+K))
                
            for i in last_arr:
                queue.append((now_str+i, now_len+1))
        
        result = sorted(result)
        return result

# 내가 구현한 방식은
# BFS로 적절하게 동작하도록(?) 구현했다.
# 1~9 의 list 를 만들때 파이토닉하게 코드를 했다.
# 적절하게 10% 로 마지막 digit 을 잘 가져와 연산했다.
# class Solution:
#     def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
#         dp = list(range(10))
        
#         if N == 1:
#             return dp
#         if K == 0:
#             pd = {"1","2","3","4","5","6","7","8","9"}
#             return [d*N for d in pd]
        
#         for i in range(1,N):
#             new = []
#             for num in dp:
#                 last = num % 10
#                 if num != 0:
#                     if last - K >= 0:
#                         new.append(10*num + last - K)
#                     if last + K <= 9:
#                         new.append(10*num + last + K)
#             dp = new
        
#         return dp