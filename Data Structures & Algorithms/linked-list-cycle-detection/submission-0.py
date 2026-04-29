# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map1 = {}

        while (head != None):
            map1[head] = map1.get(head,0)+1
            if map1[head]>1:
                return True
            head = head.next
        return False