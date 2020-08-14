# problem : Remove Linked List Elements

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
       # search head
        try:
            while head.val == val :
                head = head.next
        except AttributeError:
            return head

        now_head = head
        while now_head.next :
            if now_head.next.val == val:
                now_head.next = now_head.next.next
            else:
                now_head = now_head.next    
        
        
        return head

"""
# Dummy node 활용하여 코드 중복 제거

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
"""