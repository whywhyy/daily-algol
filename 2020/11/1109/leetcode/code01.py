# Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        if not root:
            return 0

        # with bottom up - postorder
        dump = TreeNode(left=root, right=root)
        self.postorder_sum(root, dump)

        # self.print_preorder(root)
        
        self.preorder_cal(root)

        # self.print_preorder(root)

        queue = []
        queue.append(root)

        result = 0
        while queue:
            node = queue.pop()
            result += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
        # # result = 0
    
        # # def sum_root(root):
        # #     nonlocal result
        # #     result += root.val
        # #     if root.left:
        # #         sum_root(root.left)
        # #     if root.right:
        # #         sum_root(root.right)

        # # sum_root(root)
        # # return result
        
    # # def print_preorder(self, root):
    # #     print(root.val)
    # #     if root.left:
    # #         self.print_preorder(root.left)
    # #     if root.right:
    # #         self.print_preorder(root.right)

    def travel_sum(self, root, result):
        result += root.val
        if root.left:
            self.travel_sum(root.left, result)
        if root.right:
            self.travel_sum(root.right, result)

        return result

    def postorder_sum(self, root, parent):
        if root.left:
            self.postorder_sum(root.left, root)
        if root.right:
            self.postorder_sum(root.right, root)
        
        parent.val += root.val

    def preorder_cal(self,root):
        if root.left or root.right:
            if root.left and root.right:
                root.val = abs(root.left.val - root.right.val)
            if not root.left:
                root.val = abs(root.right.val)
            if not root.right:
                root.val = abs(root.left.val)

            if root.left:
                self.preorder_cal(root.left)
            if root.right:
                self.preorder_cal(root.right)

        if not root.left and not root.right:
            root.val = 0

# 난 무얼 한것인가 !!?!?!?!
# awesome !!?
# nonlocal 을 통해 밖의 변수값을 가져와서 사용한다! 
# if not node: return 0 을 처리하기 !!!
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt

            if not node:
                return 0
            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            return left_sum + right_sum + node.val

        valueSum(root)

        return total_tilt


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        s = 0
        def get_sum(root):
            nonlocal s

            if root is None:
                return 0
            left_sum = get_sum(root.left)
            right_sum = get_sum(root.right)
            s += abs(right_sum-left_sum)
            return left_sum + root.val + right_sum

        _ = get_sum(root)
        return s

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total = 0
        
        def dfs(node):
            nonlocal total
            
            if not node:
                return 0
            
            currsum = 0
            
            #i need to keep track of sums
            #i need to calculate current node's tilt and add
            #to overall sum
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)
            
            #tilt calculation
            total += abs(leftsum - rightsum)
            
            #returning to parent the sum of my kids and my own value
            return leftsum + rightsum + node.val    
        
        dfs(root)
        return total
            

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        ans = 0
        def solve(root):
            nonlocal ans
            if root:
                left = solve(root.left)
                right = solve(root.right)
                ans += abs(left - right)
                return left + right+ root.val
            return 0
        solve(root)
        return ans