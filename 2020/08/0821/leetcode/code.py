# Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        all_node = []
        all_node.append((root, root.val))

        while queue:
            node = queue.pop()

            temp_node = node.left
            if temp_node:
                all_node.append((temp_node, temp_node.val))
                queue.append(temp_node)

            temp_node = node.right
            if temp_node:
                all_node.append((temp_node, temp_node.val))
                queue.append(temp_node)
        
        count = 0
        while all_node:
            node, value = all_node.pop()
            if value == sum:
                count +=1
            
            temp_node = node.left
            if temp_node:
                all_node.append((temp_node, value + temp_node.val))

            temp_node = node.right
            if temp_node:
                all_node.append((temp_node, value + temp_node.val))
               
        return count

# 내 코드 개선 ver
# 쪼오금 빨라졌다 1000ms -> 660ms -> if문 개선 (800ms)
# dict -> set으로 변경 820 ms
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        queue = []
        queue.append((root, root.val))
        check_set = set()

        count = 0
        while queue:
            node, value = queue.pop()
            if value == sum:
                count += 1

            for temp_node in [node.left, node.right]:
                if temp_node:
                    queue.append((temp_node, value + temp_node.val))
                    if temp_node not in check_set:
                        check_set.add(temp_node)
                        queue.append((temp_node, temp_node.val))

        return count

# 40 ms !?
# 알아보자
# 잘모르겠다..(?!)
class Solution:
    def __init__(self):
        self.total = 0
        super().__init__()
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        dic = {}
        dic[0] = 1
        self.dfs(root, 0, sum, dic)
        return self.total
        
    def dfs(self, root, carriedSum, target, dic):
        if not root:
            return
        curSum = carriedSum + root.val
        if (curSum - target) in dic:
            self.total += dic[curSum - target]
        if curSum in dic:
            dic[curSum] += 1
        else:
            dic[curSum] = 1
        self.dfs(root.left, curSum, target, dic)
        self.dfs(root.right, curSum, target, dic)
        dic[curSum] -= 1
        return
