# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        curr = head

        while curr is not None:
            if curr not in hashmap:
                hashmap[curr] = 1
                curr = curr.next
            else:
                return True

        return False