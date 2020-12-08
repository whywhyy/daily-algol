# Jump Game III
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        queue = []
        queue.append(start)
        
        # visit = set()
        visit = [False] * len(arr)
        while queue:
            idx = queue.pop()
            if arr[idx] == 0:
                return True

            if not visit[idx]:
                visit[idx] = True
                jump = arr[idx]
                if idx-jump >= 0:
                    queue.append(idx-jump)
                if idx+jump < n:
                    queue.append(idx+jump)
        
        return False

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        seen = set([start])
        
        q = [start]
        
        while q: 
            tmp =[]
            for x in q: 
                if arr[x] == 0:
                    return True 
                
                if 0<= x + arr[x] < len(arr) and x + arr[x] not in seen: 
                    
                    tmp.append(x + arr[x])
                    seen.add( x + arr[x])
                if 0<= x - arr[x] < len(arr) and  x - arr[x] not in seen:
                    tmp.append(x - arr[x])
                    seen.add(x - arr[x])
            q = tmp 
        
        return False 

# python 은 0<=x<n 가 가능하다 !
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque()
        visited = set()
        q.append(start)

        while q:
            ind = q.popleft()
            if arr[ind] == 0:
                return True
            for x in (ind-arr[ind],ind+arr[ind]):
                if 0<=x<n and x not in visited:
                    q.append(x)
                    visited.add(ind)
        return False