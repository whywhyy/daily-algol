# Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        all_left = []
        queue = []
        queue.append((root,False))
        while queue:
            now, is_left = queue.pop()
            if is_left and now.left == None and now.right == None:
                all_left.append(now.val)
            if now.left:
                queue.append((now.left, True))
            if now.right:
                queue.append((now.right,False))

        return sum(all_left)

# 항상 bfs 로 푸는데
# dfs 코드를 익혀둘 필요가 있다.
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root)
        return self.result
    
    def dfs(self, root: TreeNode):
        if root is None:
            return
        if root.left and root.left.left is None and root.left.right is None:
            self.result += root.left.val
        self.dfs(root.left)
        self.dfs(root.right)