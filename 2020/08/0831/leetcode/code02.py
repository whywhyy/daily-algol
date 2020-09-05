# Delete Node in a BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        dump = root
        parent = root
        if not root:
            return root    
    
        while dump.val != key:
            parent = dump
            if key > dump.val:
                dump = dump.right
            else:
                dump = dump.left
            if dump == None:
                return root
        
        if dump.right == None or dump.left == None:
            if dump.right == None and dump.left == None:
                if root.val == key:
                    return None
                if key > parent.val:
                    parent.right = None
                else:
                    parent.left = None
                return root
            elif dump.right == None:
                if root.val == key:
                    root = root.left
                    return root

                if key > parent.val:
                    parent.right = parent.right.left
                else:
                    parent.left = parent.left.left
                #dump = dump.left
                return root 
            elif dump.left == None:
                if root.val == key:
                    root = root.right
                    return root
                if key > parent.val:
                    parent.right = parent.right.right
                else:
                    parent.left = parent.left.right
                #dump = dump.right
                return root
        
        if dump.right.left != None:
            dump_p = dump
            dump_v = dump.right
            while dump_v.left != None:
                dump_p = dump_v
                dump_v = dump_v.left
            dump.val = dump_v.val
            dump_p.left = dump_p.left.right

        elif dump.left.right != None:
            dump_p = dump
            dump_v = dump.left
            while dump_v.right != None:
                dump_p = dump_v
                dump_v = dump_v.right
            dump.val = dump_v.val
            dump_p.right = dump_p.right.left
        else:
            if root.val == key:
                root.left.right = root.right
                root = root.left
                return root
            if key > parent.val:
                parent.right.left.right = parent.right.right
                parent.right = parent.right.left
            else:
                parent.left.left.right = parent.left.right
                parent.left = parent.left.left
        return root

# # 음!..?
# # 1. 왜 맞지..!?
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         if not root: 
#             return root
#         if root.val == key:
#             left, right = root.left, root.right
#             if left:
#                 root = p = left
#                 while p.right: 
#                     p = p.right
#                 p.right = right
#             else:
#                 root = right
#         elif root.val > key:
#             root.left = self.deleteNode(root.left, key)
#         else:
#             root.right = self.deleteNode(root.right, key)
#         return root

# # 음!? 
# # 이건또 왜 !?
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         if root:
#             if key < root.val:
#                 root.left = self.deleteNode(root.left, key)
#             elif key > root.val:
#                 root.right = self.deleteNode(root.right, key)
#             else:
#                 if root.left is None: return root.right
#                 elif root.right is None: return root.left
#                 nxt = root.right
#                 while nxt.left:
#                     nxt = nxt.left
#                 root.val = nxt.val
#                 root.right = self.deleteNode(root.right, nxt.val)
#         return root

# # 다 재귀 ㅠㅠ 
# 으렵다 ㅠㅠ
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         def successor(node: TreeNode):
#             node = node.right
#             while node.left:
#                 node = node.left
#             return node.val
#         def predecessor(node: TreeNode):
#             node = node.left
#             while node.right:
#                 node = node.right
#             return node.val
#         def helper(node, key):
#             if not node:
#                 return
#             if key > node.val:
#                 node.right = helper(node.right, key)
#             elif key < node.val:
#                 node.left = helper(node.left, key)
#             else:
#                 if not (node.left or node.right):
#                     node = None
#                 elif node.right:
#                     node.val = successor(node)
#                     node.right = helper(node.right, node.val)
#                 elif node.left:
#                     node.val = predecessor(node)
#                     node.left = helper(node.left, node.val)
#             return node

#         return helper(root, key)
    