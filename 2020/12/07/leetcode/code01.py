# Populating Next Right Pointers in Each Node II
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        child = []
        child.append(root)
        while child:
            for i in range(len(child)-1):
                child[i].next = child[i+1]
            parent = child
            child = []
            for i in range(len(parent)):
                if parent[i].left:
                    child.append(parent[i].left)
                if parent[i].right:
                    child.append(parent[i].right)

        return root

# ah ! 
# 미리 큐의 사이즈를 알고 있으니 별도의 sub queue 를 두지 않아도 된다!
# i < size-1 일때만 node.next = Q[0] 으로 next 정의
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        Q = collections.deque([root])
        while Q:
            
            size = len(Q)
            for i in range(size):
                
                node = Q.popleft()
                if i < size -1:
                    node.next = Q[0]
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root   

# 현재의 level 을 넣어 확인
# prev 노드를 기억하여 next 로 넣는다
# new level 에 도착하면 curlvl, curlvlNode = top 으로 정의
# newlevel 이 아니면 curlvlNode.next = top
class Solution:  
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        from collections import deque
        queue = deque([(root, 0)])
        curlvlNode, curlvl = None, -1
        while len(queue) != 0:
            top, lvl = queue.popleft()
            
            if lvl > curlvl: 
                curlvl = lvl
            else: 
                curlvlNode.next = top
            curlvlNode = top
            
            if top.left != None: 
                queue.append((top.left, lvl + 1))
            if top.right != None: 
                queue.append((top.right, lvl + 1))
        
        return root 

# 자식 노드들의 관계를 정의
# 현재의 next 로 이동하며 next_node 와 현재 자식의 노드들과의 관계 정의
# head_node 로 다음 level 처음 노드를 정의
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: 
            return root
        if root.left is None and root.right is None: 
            return root

        cur, head_node, next_node = root, None, None

        while cur:
            while cur:
                if cur.left:
                    if head_node is None:
                        head_node = cur.left
                        next_node = cur.left
                    else:
                        next_node.next = cur.left
                        next_node = next_node.next
                
                if cur.right:
                    if head_node is None:
                        head_node = cur.right
                        next_node = cur.right
                    else:
                        next_node.next = cur.right
                        next_node = next_node.next
                
                cur = cur.next
            cur = head_node
            head_node = None
            next_node = None
        
        return root
 
# ah ! 
# if not q:
#   q,level=level,q
#  로 q 와 level 을 swap ! 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q=collections.deque([root])
        level=collections.deque([])
        while q:
            # level=[]
            node=q.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            
            if q:
                node.next=q[0]
            if not q:
                q,level=level,q
        return root

# 위의 접근방식과 동일
# 다만, prev 노드를 현재 노드와 연결하는 방식!
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            pre = None
            for _ in range(length):
                node = queue.popleft()
                if pre is not None:
                    pre.next = node
                pre = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
        return root