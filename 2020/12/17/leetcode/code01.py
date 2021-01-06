# Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 1 1 1 1 1 1
        # 2 1 1 1 1
        # 1 2 1 1 1
        # 1 1 2 1 1
        result = []

        queue = []
        queue.append(([i for i in s],0))

        def is_palindron(arr_s):
            n = len(arr_s)
            
            if n == 1:
                return True
            else:
                for i in range(n//2):
                    if arr_s[i] != arr_s[-i-1]:
                        return False
                return True

        while queue:
            # print(queue)
            arr,start = queue.pop()
            
            check_palindron = True
            for i in arr:
                if is_palindron(i) == False:
                    check_palindron = False
                    break
            if check_palindron:
                result.append(arr)
            for i in range(start, len(arr)-1):
                front = arr[:i]
                mid = ["".join(arr[i:i+2])]
                back = arr[i+2:]
                queue.append((front + mid + back, i))
        return result


# 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start,end):
            end=end-1
            while start<end:
                if s[start]==s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True
        
        def dfs(s,start,path):
            if start==len(s):
                if path:
                    res.append(path)    
                return

            else:
                for end in range(start+1,len(s)+1):
                    if isPalindrome(start,end):
                        dfs(s,end,path+[s[start:end]])
                        
        res=[]             
        dfs(s,0,[])
        
        return res
        
        return dfs(0,len(s)-1)

# 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPal(l,r):
            while l < r:
                if s[l] != s[r]: return False
                r -= 1
                l += 1
            return True
        
        self.res = []
        
        def dfs(l,path):
            if l >= len(s): 
                self.res += [path]
            
            for r in range(l,len(s)):
                if isPal(l,r): 
                    dfs(r+1,path + [s[l:r+1]])
            
        dfs(0,[])
        return self.res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        res = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    it = res[j-1] if j >0 else [[]]
                    substr = s[j:i+1]
                    for l in it:
                        res[i].append(l + [substr])
        return res[-1] 

# awesome !!!
# 앞에서부터 n 글자가 palindrome 인지 DP 로 구현!  
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        dp = {0:[[]], 1:[[s[0]]]}
        
        for i in range(1, len(s)):
            dp[i+1] = []
            
            for j in range(0, i+1):
                if self.is_palindrome(s[j:i+1]):
                    for prev in dp[j]:
                        dp[i+1].append(prev + [s[j:i+1]])
        
        return dp[len(s)]
                
    
    def is_palindrome(self, s):
        return s == s[::-1]