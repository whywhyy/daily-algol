# Serialize and Deserialize BST
# # #
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        result = ""
        queue = deque()
        
        result += str(root.val)

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            node = queue.popleft()
            if not node:
                result += ',None'
                continue
            result += "," + str(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while len(result) >= 5 and result[-5:] == ',None':
            result = result[:-5]
        return result
        

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        data = deque(data.split(","))
        root = TreeNode(data.popleft())

        queue = deque()
        queue.append((root, 'L'))
        queue.append((root, 'R'))
        while data:
            now = data.popleft()
            node,direction = queue.popleft()

            if now == 'None':
                continue
            else:
                insert = TreeNode(now)
                if direction == 'L':
                    node.left = insert
                    insert = node.left
                else:
                    node.right = insert
                    insert = node.right
                queue.append((insert, 'L'))
                queue.append((insert, 'R'))


        return root

# serializer
# res.append 이후 ''.join(map(str,res))
# deserialize
# AH ! 
# preorder 로 str 로 구성하였으니
# desrialize 도 preorder 형식으로 build 한다.
# 따라서          v = inputs.pop(0)
#                 root = TreeNode(v)
#                 root.left = build(minv, v)
#                 root.right = build(v, maxv)
# 도 잘 동작한다.
# 
# class Codec:
#     def serialize(self, root: TreeNode) -> str:
#         """Encodes a tree to a single string.
#         """
#         res = []
#         def preorder(root):
#             if not root:
#                 return None
#             res.append(root.val)
#             preorder(root.left)
#             preorder(root.right)
#         preorder(root)
#         return ' '.join(map(str, res))
# 
#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         inputs = data.split()
#         inputs = list(map(int, inputs))
#         def build(minv,maxv):
#             if inputs and minv < inputs[0] < maxv:
#                 v = inputs.pop(0)
#                 root = TreeNode(v)
#                 root.left = build(minv, v)
#                 root.right = build(v, maxv)
#                 return root
        
#         node = build(float('-inf'), float('inf'))
#         return node

# # awesome
# class Codec:
#     def serialize(self, root):
#         """
#         Encodes a tree to a single string.
#         """
#         def postorder(root):
#             return postorder(root.left) + postorder(root.right) + [root.val] if root else []
#         return ' '.join(map(str, postorder(root)))

#     def deserialize(self, data):
#         """
#         Decodes your encoded data to tree.
#         """
#         def helper(lower = float('-inf'), upper = float('inf')):
#             if not data or data[-1] < lower or data[-1] > upper:
#                 return None
            
#             val = data.pop()
#             root = TreeNode(val)
#             root.right = helper(val, upper)
#             root.left = helper(lower, val)
#             return root
        
#         data = [int(x) for x in data.split(' ') if x]
#         return helper()


# 다들 비슷한 방식으로 구현
# class Codec:
#     def serialize(self, root: TreeNode) -> str:
#         """Encodes a tree to a single string.
#         """
#         vals = []
#         def preOrder(node):
#             if node:
#                 vals.append(node.val)
#                 preOrder(node.left)
#                 preOrder(node.right)
        
#         preOrder(root)
#         return ' '.join(map(str, vals))

#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         vals = deque(int(val) for val in data.split())
#         def build(min_val, max_val):
#             if vals and min_val < vals[0] < max_val:
#                 val = vals.popleft()
#                 node = TreeNode(val)
#                 node.left = build(min_val, val)
#                 node.right = build(val, max_val)
#                 return node
        
#         return build(float('-inf'), float('inf'))


# 눈에 뜨는 점은 list.pop() 보다는 deque.popleft 로 변경
# class Codec:

#     def serialize(self, root):
#         vals = []

#         def preOrder(node):
#             if node:
#                 vals.append(node.val)
#                 preOrder(node.left)
#                 preOrder(node.right)

#         preOrder(root)

#         return ' '.join(map(str, vals))

#     # O( N ) since each val run build once
#     def deserialize(self, data):
#         vals = collections.deque(int(val) for val in data.split())

#         def build(minVal, maxVal):
#             if vals and minVal < vals[0] < maxVal:
#                 val = vals.popleft()
#                 node = TreeNode(val)
#                 node.left = build(minVal, val)
#                 node.right = build(val, maxVal)
#                 return node

#         return build(float('-infinity'), float('infinity'))