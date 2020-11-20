# Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_arr = []
        l2_arr = []

        while l1 or l2 :
            if l1:
                l1_arr.append(l1)
                l1 = l1.next
            if l2:
                l2_arr.append(l2)
                l2 = l2.next

        i = len(l1_arr)
        j = len(l2_arr)

         
        dummy = ListNode()
        head = ListNode(val=0, next=dummy)
        while i>=1 or j>=1:
            if i>=1 and j>=1:
                head.next.val += l1_arr[i-1].val + l2_arr[j-1].val
                new_dummy = ListNode(val=0, next=head.next)
                head.next = new_dummy
                if new_dummy.next.val >= 10:
                    new_dummy.next.val %= 10
                    new_dummy.val=1
            else:
                if i >= 1:
                    head.next.val += l1_arr[i-1].val
                    new_dummy = ListNode(val=0, next=head.next)
                    head.next = new_dummy
                    if new_dummy.next.val >= 10:
                        new_dummy.next.val %= 10
                        new_dummy.val=1

                if j >= 1:
                    head.next.val += l2_arr[j-1].val
                    new_dummy = ListNode(val=0, next=head.next)
                    head.next = new_dummy
                    if new_dummy.next.val >= 10:
                        new_dummy.next.val %= 10
                        new_dummy.val=1

            i-=1
            j-=1

        if head.next.val >= 1:
            return head.next
        else:
            return head.next.next

# str로 변경 !?
# !?!?!?!
# 통짜로!? 덧셈 !!!! 
# 맞네 ㄷㄷ
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        y,c,ans = [],[], ListNode()
        #Turning listnode into list
        y.append(l1.val)
        c.append(l2.val)
        while l1.next != None:  
            l1 = l1.next
            y.append(l1.val)
        while l2.next != None:
            l2 = l2.next
            c.append(l2.val)
        #Adding both list
        y = "".join(list(map(lambda x: str(x), y))) 
        c = "".join(list(map(lambda x: str(x), c)))
        res = list(map(lambda x: x,str(int(y) + int(c))))
        temp = ans
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return ans.next

# 동짜로 덧셈 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1_str, num2_str = '', ''
        
        while l1:
            num1_str += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2_str += str(l2.val)
            l2 = l2.next
        
        ans_int = int(num1_str) + int(num2_str)
        ans_str = str(ans_int)
        
        dummy = ListNode()
        node = dummy
        
        for char in ans_str:
            new_node = ListNode()
            new_node.val = int(char)
            node.next = new_node
            node = node.next
        return dummy.next

# 통짜로 덧셈 ++
class Solution:
    def convertListToNumber(self, l):    
        number = 0
        while l != None:
            number = 10 * number + l.val
            l = l.next
        
        return number
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_number = self.convertListToNumber(l1)
        second_number = self.convertListToNumber(l2)
        
        res = str(first_number + second_number)
        
        res_list = ListNode(0)
        temp = res_list
        
        for element in res:
            temp.next = ListNode(element)
            temp = temp.next
        
        return res_list.next
# l1Stack or l2Stack or carry: 로 잘 체크함!
# v1 = l1Stack.pop().val if l1Stack else 0
# v2 = l2Stack.pop().val if l2Stack else 0
# carry = carry + v1 + v2  
# 괜찮은 접근법 인듯함 !!
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Stack = []
        l2Stack = []
        
        while l1:
            l1Stack.append(l1)
            l1 = l1.next
        
        while l2:
            l2Stack.append(l2)
            l2 = l2.next
        
        carry = 0
        node = None
        
        while l1Stack or l2Stack or carry:
            v1 = l1Stack.pop().val if l1Stack else 0
            v2 = l2Stack.pop().val if l2Stack else 0
                       
            carry = carry + v1 + v2
            temp = node
            node = ListNode(carry % 10)
            node.next = temp
            carry = carry// 10
            
        return node

# 
class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        
        head = None
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            val = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
            
        return head