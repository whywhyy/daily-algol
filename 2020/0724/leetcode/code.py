# problem : All Paths From Source to Target

import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        if graph == None:
            return res

        queue = []
        for i in range(len(graph[0])):
            now = 0
            now_graph = copy.deepcopy(graph)
            now_graph[0].pop(i)
            result = []
            result.append(0)
            result.append(graph[0][i])
            queue.append((graph[0][i],now_graph,result))
        
        while len(queue):

            now, now_graph, result = queue.pop()
            if now == len(graph) -1 :
                res.append(result)
                continue
            if len(now_graph[now]) == 0:
                continue
            for i in range(len(now_graph[now])):
                go = now_graph[now][i]
                n_graph = copy.deepcopy(now_graph)
                n_graph[now].pop(i)
                n_result = copy.deepcopy(result)
                n_result.append(go)
                queue.append((go, now_graph, n_result))

        return res

"""
# 다들 DFS 로 잘 풀었다.
# DFS 구현 특징
# 종료 조건 및 실패조건을 DFS 함수 시작부분에 작성한다.
# self.dfs 로 동작! 
# 그리고 회수(?) 하기위해 recovery 하는 동작이 있다.

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.dfs(set(), [], 0, len(graph)-1, graph)
        return self.res
        
    def dfs(self, visited, prior, node, target, graph):
        if node in visited:
            return

        if node ==  target:
            self.res.append(prior+[node])
            return 
            
        for next_node in graph[node]:
            visited.add(node)
            self.dfs(visited, prior+[node], next_node, target, graph)
            visited.remove(node)


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        visited=[False]*n
        ans=[]
        self.dfs(graph,visited,n,0,ans,[])
        return ans
    
    def dfs(self,graph,visited,n,cur,ans,path):
        path.append(cur)
        visited[cur]=True
        if(cur==n-1):
            ans.append(path[:])
        
        else:
            for v in graph[cur]:
                if(visited[v]==False):
                    self.dfs(graph,visited,n,v,ans,path)
        path.pop()
        visited[cur]=False
"""

