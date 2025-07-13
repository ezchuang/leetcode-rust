from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        counter_head = head
        counter = 0
        while counter_head:
            counter_head = counter_head.next
            counter += 1

        counter, is_odd = divmod(counter, 2)
        curr = head
        for _ in range(counter + is_odd - 1):
            curr = curr.next
        head2 = curr.next
        curr.next = None
        curr = head2

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head1 = head
        head2 = prev
        while head1 and prev:
            temp = head1.next
            head1.next = head2
            head2 = temp
            head1 = head1.next