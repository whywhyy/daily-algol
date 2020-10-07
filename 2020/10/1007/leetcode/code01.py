# Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        node_links = []
        node = head
        while node:
            node_links.append(node)
            node = node.next
        k %= len(node_links)

        node_links[-1].next = node_links[0]
        node_links[-k-1].next = None

        head = node_links[-k]
        return head