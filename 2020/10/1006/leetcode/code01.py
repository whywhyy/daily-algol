# Insert into a Binary Search Tree
# #
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root

        if not root:
            return TreeNode(val)
        while True:
            now_val = node.val
            if now_val < val:
                if node.right != None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left != None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break

        return root


# # 난 뭐한거지 ㅋㅋ;;
# # 간단 코드 
# # awesome
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return TreeNode(val)
        
#         if root.val < val:
#             root.right = self.insertIntoBST(root.right, val)
#         else:
#             root.left = self.insertIntoBST(root.left, val)
        
#         return root