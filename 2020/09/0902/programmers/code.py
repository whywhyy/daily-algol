# 섬 연결하기
from collections import defaultdict

def solution(n, costs):
    costs = sorted(costs,key=lambda x:x[2])

    total = 0

    set_list = []
    bri = defaultdict(list) 
    for i in range(len(costs)):
        s1, s2, cost = costs[i]
        if not s1 in bri or not s2 in bri:
            bri[s1].append(s2)
            bri[s2].append(s1)
            before_set = set()
            queue = []
            queue.append(s1)
            while queue:
                now_s = queue.pop()
                if not now_s in before_set:
                    before_set.add(now_s)
                for i in bri[now_s]:
                    if not i in before_set:
                        queue.append(i)
            total += cost
            if len(before_set) == n:
                return total
            continue

        # before
        before_set = set()
        queue = []
        queue.append(s1)
        while queue:
            now_s = queue.pop()
            if not now_s in before_set:
                before_set.add(now_s)
            for i in bri[now_s]:
                if not i in before_set:
                    queue.append(i)


        bri[s1].append(s2)
        bri[s2].append(s1)            
        # after
        after_set = set()
        queue = []
        queue.append(s1)
        while queue:
            now_s = queue.pop()
            if not now_s in after_set:
                after_set.add(now_s)
            for i in bri[now_s]:
                if not i in after_set:
                    queue.append(i)  
        
        if len(before_set) < len(after_set):
             total += cost
        else:
            bri[s1].pop()
            bri[s2].pop()

        if len(after_set) == n:
            return total



# # 크루스칼 알고리즘 !
# # 부모가 다르면 하나의 부모로 동일되도록 
# # 한다 ! 
# def ancestor(node, parents):
#     if parents[node] == node:
#         return node
#     else:
#         return ancestor(parents[node], parents)

# def solution(n, costs):
#     answer = 0
#     edges = sorted([(x[2], x[0], x[1]) for x in costs])
#     parents = [i for i in range(n)]
#     bridges = 0
#     for w, f, t in edges:
#         if ancestor(f, parents) != ancestor(t, parents):
#             answer += w
#             parents[ancestor(f, parents)] = t
#             bridges += 1
#         if bridges == n - 1:
#             break
#     return answer