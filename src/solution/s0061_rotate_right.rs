use crate::util::linked_list::ListNode;

pub struct Solution;

impl Solution {
    // https://leetcode.com/problems/rotate-list/solutions/3593450/rust-solution-o-1-space-o-n-time/
    pub fn rotate_right(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref()?.next.is_none() {
            return head;
        }

        let mut cnt = 0;
        let mut node_ref = head.as_ref();

        while let Some(node) = node_ref {
            cnt += 1;
            node_ref = node.next.as_ref();
        }

        let k = k % cnt;
        if k == 0 { return head; }
        
        
        let mut curr_ref = head.as_deref_mut().unwrap();
        for _ in 0..cnt - k - 1  {
            curr_ref = curr_ref.next.as_deref_mut().unwrap();
        }
        
        let mut new_head = curr_ref.next.take().unwrap();
        
        curr_ref = new_head.as_mut();
        while curr_ref.next.is_some() {
            curr_ref = curr_ref.next.as_deref_mut().unwrap();
        }

        curr_ref.next = head;

        Some(new_head)
    }
}