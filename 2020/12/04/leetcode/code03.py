# Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # with dfs
       
        self.result = 0
        def dfs(node,num):
            self.result = max(self.result, num)
            if not node:
                return None
            dfs(node.left, num+1)
            dfs(node.right, num+1)

        dfs(root, 0)
        return self.result

# 개선 ver
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # with dfs
       
        self.result = 0
        def dfs(node,num):
            if node:
                dfs(node.left, num+1)
                dfs(node.right, num+1)
            if node and not node.left and not node.right:       
                self.result = max(self.result, num+1)
        
        dfs(root, 0)
        return self.result

# 개선 ver 2... fail..
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # with dfs
       
        self.result = 0
        def dfs(node,num):
            if not node:
                return None
            dfs(node.left, num+1)
            dfs(node.right, num+1)
            self.result = max(self.result, num+1)

        dfs(root, 0)
        return self.result


# good last i 값으로 결과 !
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        d = deque()
        d.append((0, root))
        
        while d:
            i, t = d.popleft()
            if t:
                i += 1
                d.append((i, t.left))
                d.append((i, t.right))
        return i

# good  
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def getDepth(current_node: TreeNode, current_depth: int) -> int:
            # get the depth of the left branch
            if current_node.left is not None:
                left_depth = getDepth(current_node.left, current_depth+1)
            else:
                left_depth = current_depth
                
            # get the depth of the right branch
            if current_node.right is not None:
                right_depth = getDepth(current_node.right, current_depth+1)
            else:
                right_depth = current_depth
            
            return max(left_depth, right_depth)
        
        if root is None:
            return 0
        
        return getDepth(root, 1)

# awesome 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1+max(left,right)