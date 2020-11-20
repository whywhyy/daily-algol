# Minimum Height Trees
# https://www.youtube.com/watch?v=OsvbLAaRmu8

# 개선 전
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        path = defaultdict(list)
        for i in edges:
            start, end = i
            path[start].append(end)
            path[end].append(start)

        # delete leaf node 
        
        leaves = [ i for i in path if len(path[i]) ==1 ]
        while n > 2:
            n -= len(leaves)
            
            for i in leaves:
                now_leaf = path[i]
                path.pop(i)
                path[now_leaf[0]].remove(i)
                    
            # print(path)
            leaves = [ i for i in path if len(path[i]) ==1 ]

        return [ i for i in path]

# awesome 
# leaf 노드를 하나씩 제거하는 방식으로 구현
# leaf 에 결국 남아있는게 정답!? 
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        path = defaultdict(list)
        for i in edges:
            start, end = i
            path[start].append(end)
            path[end].append(start)

        # delete leaf node 
        
        leaves = [ i for i in path if len(path[i]) ==1 ]
        while n > 2:
            n -= len(leaves)
            
            new_leaves = set()
            for i in leaves:
                neighnor = path[i].pop()
                path[neighnor].remove(i)
                if len(path[neighnor]) == 1:
                    new_leaves.add(neighnor)
            
            leaves = new_leaves
            # leaves = [ i for i in path if len(path[i]) ==1 ]

        return leaves