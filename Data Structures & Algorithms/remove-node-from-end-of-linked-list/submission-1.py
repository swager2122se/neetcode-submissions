# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr =head
        prev = None
        # reversing the linked list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # return prev

        
        toDelete = prev

        if n == 1:
            prev = prev.next
        
        while n > 2:
            toDelete = toDelete.next
            n -=1

        if toDelete.next:
            toDelete.next = toDelete.next.next 
        

        
        curr =prev
        prev = None
        # reversing the linked list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        return prev

            