# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # Find the middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        while second_half is not None:
            nxt = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = nxt
        
        second_half = prev

        # Merge the two halves
        while second_half is not None:
            first_half_nxt = head.next
            second_half_nxt = second_half.next
            head.next = second_half
            second_half.next = first_half_nxt
            head = first_half_nxt
            second_half = second_half_nxt




