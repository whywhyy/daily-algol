# Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inc_arr = []

        def search_inc(node):
            if node.left:
                search_inc(node.left)
            inc_arr.append(node)
            if node.right:
                search_inc(node.right)

        search_inc(root)
        for i in range(len(inc_arr)-1):
            inc_arr[i].right = inc_arr[i+1]
            inc_arr[i].left = None

        inc_arr[-1].left = None
        inc_arr[-1].right = None
        return inc_arr[0]

# skip .. 
class Solution:
    head = None
    prev = None
    def increasingBST(self, root: TreeNode,newT=True) -> TreeNode:
        if newT == True:
            self.head = None
            self.prev = None
        if root == None:
            return None
        self.increasingBST(root.left,False)
        if self.prev == None:
            self.head = root
        else:
            root.left = None
            self.prev.right = root
        self.prev = root
        self.increasingBST(root.right,False)
        return self.head

# simple good
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

# 값만 받아 ringt 에 input
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal temp
            if not node:
                return

            inorder(node.left)
            temp.right = TreeNode(node.val)
            temp = temp.right
            inorder(node.right)

        result = TreeNode(0)
        temp = result
        inorder(root)

        return result.right

# hmm good
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        global roots
        roots=root
        global first
        global joiner
        joiner = None
        first = 1

        def helper(nde):
            global first
            global roots
            global joiner
            if nde.left:
                helper(nde.left)
            if first:
                roots = nde
                joiner = nde
                first = 0
            else:
                nde.left = None
                joiner.right = nde
                joiner = nde
            if nde.right:
                helper(nde.right)

        helper(roots)
        return roots