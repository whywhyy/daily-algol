# Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next

        arr = sorted(arr, key = lambda x : x.val)
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        
        arr[-1].next = None
        return arr[0]

# Awesome
# #
# Linked List 에서도 Merge Sort가 가능하다 !
# # 
# if not head or not head.next:
# 이유 : 다음 노드가 없거나, 다음노드가 존재하지 않으면 return head
# 즉, 2개이상의 노드만 가능!
# #
# l, r = self.sortList(head), self.sortList(r_node)
# 이유 : merge sort 하기위한 각각의 첫번째 노드
# #
# merge : merge sort !
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next # only two corner case
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        r_node = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(r_node)
        return self.merge(l, r)
        
    def merge(self, l, r):
        dummy = ListNode()
        cur_node = dummy
        while l and r:
            if l.val < r.val:
                cur_node.next = l
                cur_node, l = cur_node.next, l.next
            else:
                cur_node.next = r
                cur_node, r = cur_node.next, r.next
        if l:
            cur_node.next = l
        if r:
            cur_node.next = r
        return dummy.next