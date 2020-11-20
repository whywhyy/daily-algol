# 1627. Graph Connectivity With Threshold

# https://www.youtube.com/watch?v=Y2DIq4qG9pw
# union find 
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold == 0:
            return [True]*len(queries)

        par = [x for x in range(n+1)]

        def ufind(x):
            if x != par[x]:
                par[x] = ufind(par[x])
            return par[x]

        def uunion(a, b):
            pa = ufind(a)
            pb = ufind(b)

            par[pa] = pb
        
        # x 배와 같다면 같은 union 으로 묶는다 ! 
        # 3- 3,6,9,12~~
        # 4- 4,8,12,16~~
        # par[3] = 3
        # par[3] = 6 , par[6] = 6
        # par[3] = 6 , par[6] = 9, par[9] = 9
        # 가장 큰값이 root 로 해야 같은 set 인지 확인 가능하다!
        for x in range(threshold + 1, n+1):
            k = x
            while k <= n:
                uunion(x,k)
                k += x
        # print(par)
        
        return [ufind(a) == ufind(b) for a,b in queries]


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
        par = list(range(0, n+1))
        
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
                
            return par[x]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            par[pa] = pb
            return True
        
        for i in range(threshold+1, n+1):
            # general idea: i is the common divisor,
            # j is the multiple of i 
            # so only union these type of relationships
            for j in range(2*i, n+1, i):
                union(i, j)
            
        out = []
        for a, b in queries:
            if find(a) == find(b):
                out.append(True)
            else:
                out.append(False)
                
        return out

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
        if threshold == 0:
            return [True for _ in queries]
        
        parent = [i for i in range(n + 1)]
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            parent[root_b] = root_a
        
        for base in range(2, n):
            if base <= threshold:
                continue
            for x in range(base, n + 1, base):
                union(base, x)

        return [find(a) == find(b) for a, b in queries]