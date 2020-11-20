# Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        result = 0

        node = root

        queue = []
        queue.append((root,root.val,root.val))

        while queue:
            now_node, max_v, min_v = queue.pop()

            result = max(result, max_v-min_v)
            if now_node.left:
                max_l = max(max_v, now_node.left.val)
                min_l = min(min_v, now_node.left.val)
                queue.append((now_node.left, max_l, min_l))
            
            if now_node.right:
                max_r = max(max_v, now_node.right.val)
                min_r = min(min_v, now_node.right.val)
                queue.append((now_node.right, max_r, min_r))

        return result

# 역시나 (!?) 내앞에는 DFS
# left 의 최대 차이값, right 의 최대 차이값을 DFS로 탐색
        # def dfs(root, mx = mx, mn = mn):
        #     if not root: 
        #         return abs(mx-mn)
        #     left = dfs(root.left, max(mx, root.val), min(mn, root.val))
        #     right = dfs(root.right, max(mx, root.val), min(mn, root.val))
        #     return max(left, right)
# if not root: return abs(mx-mn) 으로 정지 조건 구현!
class Solution:
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        mx, mn = -inf, inf
        def dfs(root, mx = mx, mn = mn):
            if not root: 
                return abs(mx-mn)
            left = dfs(root.left, max(mx, root.val), min(mn, root.val))
            right = dfs(root.right, max(mx, root.val), min(mn, root.val))
            return max(left, right)
        res = dfs(root)
        return res

# parent min, max 를 가져와서 내껄 계산 !
# 아래 자식에게는 내 정보만 넘겨준다 ! 아래에서 알아서 계산 !!
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack = [(root, root.val, root.val)]
        res = float('-inf')
        
        while stack:
            node, parent_max, parent_min = stack.pop()
            res = max([res, abs(parent_max - node.val), abs(parent_min - node.val)])
            parent_max = max(parent_max, node.val)
            parent_min = min(parent_min, node.val)
            if node.left:
                stack.append((node.left, parent_max, parent_min))
            if node.right:
                stack.append((node.right, parent_max, parent_min))
        
        return res

# 처음에만 동작 하는 코드 !
# 
# max(max_diff, abs(node.val - min_v),abs(node.val -max_v )) 로 계산해버린다!
# if node.left is not None : 로 left 확인 ! 
# node.left 보다 빠른듯!?
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, None, None)]
        max_diff = 0
        while len(stack) != 0:
            node, min_ancestor, max_ancestor = stack.pop()
            if min_ancestor is None:
                if node.left is not None:
                    stack.append((node.left, node, node))
                if node.right is not None:
                    stack.append((node.right, node, node))
            else:
                max_diff = max(max_diff, abs(node.val - min_ancestor.val), abs(node.val - max_ancestor.val))
                if node.left is not None:
                    stack.append((node.left,
                                  node if node.val < min_ancestor.val else min_ancestor,
                                  node if node.val > max_ancestor.val else max_ancestor))
                if node.right is not None:
                    stack.append((node.right,
                                  node if node.val < min_ancestor.val else min_ancestor,
                                  node if node.val > max_ancestor.val else max_ancestor))
        return max_diff