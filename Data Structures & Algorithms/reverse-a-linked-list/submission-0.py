# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        before = None
        while trav != None:
            after = trav.next
            trav.next = before
            before = trav
            trav = after
        head = before
        return head