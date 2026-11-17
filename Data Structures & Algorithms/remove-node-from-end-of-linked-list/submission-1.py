# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        count = 0
        while count < n:
            first = first.next
            count += 1
        
        dummy = ListNode()
        dummy.next = head
        second, secnext = dummy, head

        while first:
            first = first.next
            second = secnext
            secnext = secnext.next
        
        second.next = second.next.next
        return dummy.next
        