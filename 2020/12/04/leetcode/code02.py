# Linked List Random Node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.val_list = []
        node = head
        while node:
            self.val_list.append(node.val)
            node = node.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        return self.val_list[random.randint(0,len(self.val_list)-1)]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()