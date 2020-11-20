# Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        node = head
        node_link = []
        while node:
            node_link.append(node)
            node = node.next
        # with sort 40ms
        node_link = sorted(node_link, key=lambda x: x.val)
        for i in range(len(node_link)-1):
            node_link[i].next = node_link[i+1]
        node_link[-1].next = None
        return node_link[0]
        
        # with insert sort 4760ms
        # for i in range(len(node_link)):
        #     now_node = node_link[i]
        #     j = i
        #     while j and node_link[j-1].val > node_link[j].val:
        #         node_link[j].val, node_link[j-1].val = node_link[j-1].val, node_link[j].val
        #         j -= 1
        # return head

# 1508 ms insert sort 
# 새로운 노드 후 맨뒤로 보내기 ! 
# dummy next 이후로 insert 하기 !!
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        
        curr = head
        
        while curr:
            
            prev = dummy
            nextnode = prev.next
                     
            while nextnode:
                if curr.val < nextnode.val:
                    break
                prev = nextnode
                nextnode = nextnode.next
            nextiter = curr.next
            curr.next = nextnode
            prev.next = curr
            
            curr = nextiter

        return dummy.next