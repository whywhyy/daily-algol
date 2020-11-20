# Minimum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0

        node = root
        queue = deque()
        queue.append((root,1))
        while queue:
            now, result = queue.popleft()
            if now.left:
                queue.append((now.left,result+1))
            if now.right:
                queue.append((now.right,result+1))
            if not now.left and not now.right:
                return result

# 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
# List 로 빠르게 동작 하는듯 !
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        depth = 0
        nextLevel = [root]
        while True:
            level = nextLevel
            depth += 1
            nextLevel = []
            for n in level:
                found = False
                if n.left:
                    nextLevel.append(n.left)
                    found = True
                if n.right:
                    nextLevel.append(n.right)
                    found = True
                if not found:
                    return depth
        return 0


# stack 으로 모든결과 res에 input 후 min(res)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        res = []
        stack = [(root, 1)]
        
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls)
            if node.right:
                stack.append((node.right, ls+1))
            if node.left:
                stack.append((node.left, ls+1))
        
        return min(res)

# 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftChild = rightChild = 0
        if root.left:
            leftChild = self.minDepth(root.left)
        if root.right:
            rightChild = self.minDepth(root.right)
            
        if leftChild and not rightChild:
            return 1 + leftChild
        elif rightChild and not leftChild:
            return 1 + rightChild
        else:
            return min(leftChild+1,rightChild+1)