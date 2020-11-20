# Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 240ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # sum[low, high]
        node = root
        queue = []
        queue.append(node)

        result = 0
        while queue:
            node = queue.pop()
            
            if node.val >= low and node.val <= high:
                result += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result


# 208 ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # sum[low, high]
        node = root
        queue = []
        queue.append(node)

        result = 0
        while queue:
            node = queue.pop()
            
            # if node.val >= low and node.val <= high:
            # 아래와 같이 가능 !!
            if low <= node.val <= high:
                result += node.val

            if node.left and node.val >= low:
                queue.append(node.left)
            if node.right and node.val <= high:
                queue.append(node.right)
        
        return result