# Sum of Root To Leaf Binary Numbers

# int(bin,2) => 32ms
# with *2 => 36 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = 0 
        queue = []
        # queue.append((root, str(root.val)))
        queue.append((root, root.val))

        while queue:
            node, val = queue.pop()
            if node.left == None and node.right == None:
                # result += int(val,2)
                result += val
            if node.left:
                queue.append((node.left, val*2 + node.left.val))
                # queue.append((node.left, val+str(node.left.val)))
            if node.right:
                queue.append((node.right, val*2 + node.right.val))
                # queue.append((node.right, val+str(node.right.val)))
        return result