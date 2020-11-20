# Longest Mountain in Array
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        prev = arr[0]
        j = 1
        while j < len(arr):
            step = 1
            # up
            if j < len(arr):
                if prev < arr[j]:
                    while j < len(arr) and prev < arr[j]:
                        step +=1
                        prev = arr[j]
                        j+=1
                else:
                    prev = arr[j]
                    j+=1
                    continue

            # top
            # down
            if j < len(arr):
                if prev > arr[j]:
                    while j < len(arr) and prev > arr[j]:
                        step +=1
                        prev = arr[j]
                        j+=1
                    result = max(result, step)
                else:
                    prev = arr[j]
                    j+=1
                    continue
            
        return result

# Longest Mountain in Array
# 살짝(!?) 개선
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        prev = arr[0]
        j = 1
        while j < len(arr):
            step = 1
            
            if j < len(arr):
                if prev < arr[j]:
                    # up
                    while j < len(arr) and prev < arr[j]:
                        step +=1
                        prev = arr[j]
                        j+=1
                    # top
                    # down
                    if j < len(arr) and prev > arr[j]:
                        while j < len(arr) and prev > arr[j]:
                            step +=1
                            prev = arr[j]
                            j+=1
                        result = max(result, step)
                else:
                    prev = arr[j]
                    j+=1
        return result

# i 로 산오르는 커서 !
# base 는 기존 시작점!
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans = 0
        base = 1
        l = len(A)
        
        while(base < l):
            i = base
            if(i < l and A[i] > A[i-1]):
                while(i < l and A[i] > A[i-1]):
                    i = i + 1
                    #print("asc: " + str(i))
                if(i < l and A[i-1] > A[i]):
                    while(i < l and A[i] < A[i-1]):
                        i = i + 1
                        #print("desc: " + str(i))
                    ans = max(ans, i - base + 1)  
            base = max(i, base + 1)
            
        return ans

# 산의 시작부분을 찾는다!
# 모르게따 ;;
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        mountain_len = 0
        j = 1 # fast pointer
        i = j - 1 # slow pointer, start index of mountain
        while j < N:
            while j < N and A[j] > A[j-1]:
                j += 1
            # A[j-1] > A[i], peak > start of mountain
            if A[j-1] > A[i] and j < N and A[j] < A[j-1]:
                while j < N and A[j] < A[j-1]:
                    j += 1
                j -= 1 # end index of mountain
                L = j - i + 1
                if j < N and A[j] < A[j-1] and L >= 3 and L > mountain_len:
                    mountain_len = L
            j += 1
            i = j - 1
        return mountain_len

# 정상부분을 먼저 찾는다!
# left rigt 로 이동하며 길이찾기 !
class Solution:
    def longestMountain1pass(self, A: List[int], res=0) -> int:    
        for i in range(1, len(A) - 1):
            if A[i + 1] < A[i] > A[i - 1]:
                l = r = i
                while l and A[l] > A[l - 1]:
                    l -= 1
                while r + 1 < len(A) and A[r] > A[r + 1]:
                    r += 1
                if r - l + 1 > res: 
                    res = r - l + 1
        return res
    
    def longestMountain_follow_up(self, A: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: 
                up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: 
                res = max(res, up + down + 1)
        return res
    
    def longestMountain(self, A: List[int]) -> int:
        #return self.longestMountain_follow_up(A)
        return self.longestMountain1pass(A)


# was 가 초기화 잘 되지 않아보이지만
# 동작한다. 상태기반!
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        lastup = lastdown = ans = was = 0
        for i in range(1, len(A)):
            if A[i]-A[i-1] > 0:
                lastdown = 0
                lastup += 1
            elif A[i]-A[i-1] < 0:
                if lastup > 0:
                    was = lastup + 1
                lastup = 0
                lastdown += 1
                if was > 0:
                    ans = max(ans, was+lastdown)
            else:
                lastdown = 0
                lastup = 0
                was = 0
        return ans

# 
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A: 
            return 0
        state = 0 # or 1 
        last_num = A[0]
        cur_len = 1
        longest = 0
        for i in range(1, len(A)):
            if state:
                #state == 1 means decreasing trend
                if A[i] < last_num:
                    cur_len += 1
                elif A[i] == last_num:
                    longest = max(longest, cur_len)
                    cur_len = 1
                    state = 0
                else:
                    longest = max(longest, cur_len)
                    cur_len = 2
                    state = 0
            else:
                #state == 0 means increasing trend
                if A[i] > last_num:
                    cur_len += 1
                elif A[i] == last_num:
                    cur_len = 1
                else:
                    if cur_len >= 2:
                        state = 1
                        cur_len += 1
                    else:
                        cur_len = 1
            last_num = A[i]
        if state:
            longest = max(longest, cur_len)
        
        return longest


# 
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        res = 0
        up = down = False
        count = 0
        for i in range(len(A) - 1):
            delta = A[i+1] - A[i]
            if delta > 0:
                if up:
                    count += 1
                else:
                    down = False
                    up = True
                    res = max(res, count)
                    count = 2
            elif delta < 0:
                if up:
                    up = False
                    down = True
                    count += 1
                elif down:
                    count += 1
            else:
                if down:
                    res = max(res, count)
                count = 0
                up = down = False
        if down:
            res = max(res, count)
        return res

# 
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        prev = None
        climb = True
        longest = 0
        cur = 0
        for x in A:
            if prev is None:
                prev = x
                continue
            if x == prev:
                if not climb:
                    longest = max(cur, longest)
                climb = True
                cur = 0
                continue
            if x > prev:
                if climb:
                    cur += 1
                else:
                    longest = max(cur, longest)
                    climb = True
                    cur = 1
            if x < prev:
                if climb and cur > 0:
                    climb = False
                    cur += 1
                elif not climb:
                    cur += 1
                else:
                    longest = max(cur, longest)
                    cur = 0
            prev = x
        if not climb:
            longest = max(cur, longest)
        if longest > 0:
            return longest + 1
        return 

# 
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        prev = None
        climb = True
        longest = 0
        cur = 0
        for x in A:
            if prev is None:
                prev = x
                continue
            if x == prev:
                if not climb:
                    longest = max(cur, longest)
                climb = True
                cur = 0
                continue
            if x > prev:
                if climb:
                    cur += 1
                else:
                    longest = max(cur, longest)
                    climb = True
                    cur = 1
            if x < prev:
                if climb and cur > 0:
                    climb = False
                    cur += 1
                elif not climb:
                    cur += 1
                else:
                    longest = max(cur, longest)
                    cur = 0
            prev = x
        if not climb:
            longest = max(cur, longest)
        if longest > 0:
            return longest + 1
        return 0

# 
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up=0
        down=0
        ans=0
        for i in range(0,len(A)-1):
            if A[i]<A[i+1]:
                if down==0:
                    up+=1
                else:
                    up=1
                    down=0
                    
            elif A[i]>A[i+1]:
                if up>0:
                    down+=1
                    mountain=up+down+1
                    if ans<mountain:
                        ans=mountain
                
            else:
                up=0
                down=0

            
        return ans