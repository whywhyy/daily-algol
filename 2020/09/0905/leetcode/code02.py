# All Elements in Two Binary Search Trees

# Definition for a binary tree node.
# 현재 : 348 ms (with sort) 
# # without sort => 396 ms ;;
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]: 
        root1_arr = []
        root2_arr = []
        if root1:
            self.dfs(root1,root1_arr)
        if root2:
            self.dfs(root2,root2_arr)
        
        if not root1_arr:
            return root2_arr
        if not root2_arr:
            return root1_arr
        
        root1_cur = 0
        root2_cur = 0
        
        result = []
        # while root1_cur < len(root1_arr) and root2_cur < len(root2_arr):
        #     if root1_arr[root1_cur] <= root2_arr[root2_cur]:
        #         result.append(root1_arr[root1_cur])
        #         root1_cur += 1
        #     else:
        #         result.append(root2_arr[root2_cur])
        #         root2_cur += 1

        # if root1_cur != len(root1_arr):
        #     return result + root1_arr[root1_cur:]
        # else:
        #     return result + root2_arr[root2_cur:]
        
        result = sorted(root1_arr + root2_arr)
        return result
    
    def dfs(self,root,arr):
        if root.left != None:
            self.dfs(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.dfs(root.right,arr)
        

# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         l1, stack1, root = [], [], root1
#         while stack1 or root:
#             # 해당 노드에서 left 끝까지!
#             while root:
#                 stack1.append(root)
#                 root = root.left
#             # stack 에서 하나 뺴서 right 로 !
#             # right 끝까지!
#             root = stack1.pop()
#             l1.append(root.val)
#             root = root.right
#         l2, stack2, root = [], [], root2
#         while stack2 or root:
#             while root:
#                 stack2.append(root)
#                 root = root.left
#             root = stack2.pop()
#             l2.append(root.val)
#             root = root.right
#         l = l1 + l2
#         return sorted(l)