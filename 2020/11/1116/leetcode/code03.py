# Populating Next Right Pointers in Each Node
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        parent = []
        parent.append(root)

        while parent:
            child = []
            for p in parent:
                if p.left or p.right:
                    if child:
                        child[-1].next = p.left
                    child.append(p.left)
                    child.append(p.right)
                    child[-2].next = child[-1]
                else:
                    break

            parent = child
        
        return root

# parent 노드에서 child 의 next 정의 
# 이후 현재의 next가 존재하면 next 로 이동! 
# 완료 된다면 curr = curr.lest 로 이동 !!
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        curr = root
        while curr.left:
            lvl_nodes = curr
            prev_node = None
            while lvl_nodes:
                if prev_node:
                    prev_node.next = lvl_nodes.left
                lvl_nodes.left.next = lvl_nodes.right
                prev_node = lvl_nodes.right
                lvl_nodes = lvl_nodes.next
            curr = curr.left
            
        return root

# 옿 잘동작하는구나!
# len(queue) 는 지속적으로 정의되지 않고 한번만 확인(!?) 한다!?
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])
        while queue:
            for idx in range(len(queue)-1):
                queue[idx].next = queue[idx+1]
            
            for _ in range(len(queue)):
                cur= queue.popleft()
                if cur and cur.left and cur.right:
                    queue.append(cur.left)
                    queue.append(cur.right)
        return root

# 자식 노드가 존재할때 
# 부모노드를 이용하여 !
class Solution:
    def connect(self, root):
      leftNode = root
      while leftNode and leftNode.left:
        self.populateLowerLevel(leftNode)
        leftNode = leftNode.left
      return root
    
    def populateLowerLevel(self, startNode):
      i = startNode
      while i is not None:
        i.left.next = i.right
        if i.next is not None:
          i.right.next = i.next.left        
        i = i.next