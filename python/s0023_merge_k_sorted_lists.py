from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val_arr = []
        for l in lists:
            while l:
                val_arr.append(l.val)
                l = l.next
        
        dummy = ListNode(0)
        curr = dummy
        for v in sorted(val_arr):
            curr.next = ListNode(v)
            curr = curr.next
        
        return dummy.next