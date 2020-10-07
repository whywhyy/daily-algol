# Evaluate Division
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(dict)
        result = []

        for (start, end), val in zip(equations, values):
            path[start][end] = val
            path[end][start] = 1.0 / val
        
        
        for i in queries:
            start, end = i
            queue = []

            for j in path[start]:
                queue.append((j, path[start][j], set([j])))
            
            if not queue:
                result.append(-1)
                continue

            while queue:
                now, val,now_set = queue.pop()
                if now == end:
                    result.append(val)
                    break

                for j in path[now]:
                    if j not in now_set:
                        insert_set = now_set
                        insert_set.add(j)
                        queue.append((j,  path[now][j]*val, insert_set))

                if not queue:
                    result.append(-1)

        return result

# awesome 하다
# Floyd Warshal 이라니!?
import itertools as it
class Solution:
    # Floyd Warshal:
    def calcEquation(self, equations, values, queries) -> List[float]:
        q = defaultdict(dict)        
        for (a, b), v in zip(equations, values):
            q[a][a] = q[b][b] = 1.0
            q[a][b] = v
            q[b][a] = 1 / v
        for k, j, i in it.permutations(q, 3):
            if k in q[i] and j in q[k]:
                q[i][j] = q[i][k] * q[k][j]
            
        return [q[a].get(b, -1.0) for a, b in queries]

# DFS
# 안되는 종료조건, 되는(?) 종료조건, DFS 및 결과를 return
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(defaultdict)
        for (src, dest), val in zip(equations, values):
            graph[src][dest] = val
            graph[dest][src] = 1.0 / val
            
        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0
            if dest in graph[src]:
                return graph[src][dest]
            for i in graph[src]:
                if i not in visited:
                    visited.add(i)
                    intermediate = dfs(i, dest, visited)
                    if intermediate == -1:
                        continue
                    else:
                        return graph[src][i] * intermediate
            return -1.0
        
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res