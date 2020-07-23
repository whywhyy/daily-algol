# problem : Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = {}
        r_stack = []
        l_stack = []
        # insert - input result / right first
        # pop - input result / left first
        l_stack.append((root,0))

        while len(l_stack) or len(r_stack):
            if len(r_stack):
                len_r = len(r_stack)
                for i in range(len_r):
                    a = r_stack.pop()
                    try:
                        result[a[1]].append(a[0].val)
                    except:
                        result[a[1]] = []
                        result[a[1]].append(a[0].val)
                    if a[0].right != None:
                        l_stack.append((a[0].right,a[1]+1))
                    if a[0].left != None:
                        l_stack.append((a[0].left,a[1]+1))
            if len(l_stack):
                len_r = len(l_stack)
                for i in range(len_r):
                    a = l_stack.pop()
                    try:
                        result[a[1]].append(a[0].val)
                    except:
                        result[a[1]] = []
                        result[a[1]].append(a[0].val)
                    if a[0].left != None:
                        r_stack.append((a[0].left,a[1]+1))
                    if a[0].right != None:
                        r_stack.append((a[0].right,a[1]+1))
        real_result = []

        for i in range(len(result)):
            real_result.append(result[i])
        return real_result
            

"""
# tree 순회에 익숙해지기위해 머리를 잘 굴려야겠다..(?)..

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res= []
        queue=deque([(root, 1)])
        while queue:
            reslist = []
            for i in range(len(queue)):
                curr, level = queue.popleft()
                if level % 2 == 1:
                    reslist.append(curr.val)
                else:
                    reslist.insert(0, curr.val)
                if curr.left:
                    queue.append((curr.left, level+1))
                if curr.right:
                    queue.append((curr.right, level+1))
            res.append(reslist)
        return res
"""

