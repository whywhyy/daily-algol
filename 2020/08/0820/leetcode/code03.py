#  Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        all_val = []
        if head is None:
            return []
        dummy = ListNode()
        dummy.next = head
        
        while dummy.next:
            dummy = dummy.next
            all_val.append(dummy.val)
        
        dummy  = ListNode(123456,None)
        dummy.next = head

        head_dummy = dummy
        count = 0
        for i in range(len(all_val)-1,len(all_val)//2-1,-1):
            if count == i:
                dummy.next = ListNode(all_val[i],None)
                dummy = dummy.next
                break
            dummy.next = ListNode(all_val[count],None)
            dummy = dummy.next
            dummy.next = ListNode(all_val[i],None)
            dummy = dummy.next
            count += 1

        head.next = head_dummy.next.next

# 이게 왜 맞지.?
# 일단 dictionary 로 prev 를 잘 정의했다!
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         prevs = {}
#         node = head
#         prev = None
#         while node:
#             prevs[node] = prev
#             prev = node
#             node = node.next
#         tail = prev
#         while head and tail:
#             if head == tail:
#                 head.next = None
#                 return
#             temp_head = head.next
#             head.next = tail
#             if prevs[tail] == head:
#                 tail.next = None
#                 return
#             tail.next = temp_head
#             head = temp_head
#             tail = prevs[tail]
#         return head