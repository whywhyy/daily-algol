# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        result = 0

        while node:
            result *= 2
            result += node.val
            node = node.next
        
        return result

# str to int(a,2)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = ""
        while head:
            a = a + str(head.val)
            head =  head.next
        
        return int(a,2)

# binary str to int 
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        val = -1
        binary_value = ""
        while current:
            binary_value=str(current.val) +binary_value
            current = current.next
        val =0
        for position in range(0,len(binary_value)):
            val+=int(binary_value[position])*(2**position)
        return val