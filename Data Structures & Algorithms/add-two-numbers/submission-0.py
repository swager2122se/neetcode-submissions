# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        k = 0
        n1 = 0
        while l1:
            
            n1 += 10**k * l1.val
            l1 = l1.next
            k +=1
        

        a = 0
        n2=0

        while l2:
            
            n2 += 10**a* l2.val
            l2 = l2.next
            a +=1
        
        n3 = n1+n2

        if n3 == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current = dummy
        while n3 > 0:
            current.next = ListNode(n3 % 10)
            current = current.next
            n3 //= 10
        return dummy.next
        

        