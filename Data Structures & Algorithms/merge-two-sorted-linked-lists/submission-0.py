# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        a_pointer, b_pointer = list1, list2
        curr = head
        while a_pointer and b_pointer:
            if a_pointer.val <= b_pointer.val:
                curr.next = a_pointer
                a_pointer = a_pointer.next
            else:
                curr.next = b_pointer
                b_pointer = b_pointer.next
            curr = curr.next
        
        while a_pointer:
            curr.next = a_pointer
            a_pointer = a_pointer.next
            curr = curr.next

        while b_pointer:
            curr.next = b_pointer
            b_pointer = b_pointer.next
            curr = curr.next
        
        return head.next

        