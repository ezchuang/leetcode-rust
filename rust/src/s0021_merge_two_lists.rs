pub struct Solution {}

use crate::util::linked_list::ListNode;

impl Solution {
    // try not to mutate parameters
    // pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     let (mut list1, mut list2) = (list1.as_ref(), list2.as_ref());
    //     let mut dummy_head = Box::new(ListNode::new(0));
    //     let mut curr = &mut dummy_head;

    //     while let (Some(list1_node), Some(list2_node)) = (list1, list2) {
    //         if list1_node.val <= list2_node.val {
    //             curr.next = Some(Box::new(ListNode::new(list1_node.val)));
    //             list1 = list1_node.next.as_ref();
    //         } else {
    //             curr.next = Some(Box::new(ListNode::new(list2_node.val)));
    //             list2 = list2_node.next.as_ref();
    //         }
    //         curr = curr.next.as_mut().unwrap();
    //     }

    //     while let Some(list1_node) = list1 {
    //         curr.next = Some(Box::new(ListNode::new(list1_node.val)));
    //         list1 = list1_node.next.as_ref();
    //         curr = curr.next.as_mut().unwrap();
    //     }

    //     while let Some(list2_node) = list2 {
    //         curr.next = Some(Box::new(ListNode::new(list2_node.val)));
    //         list2 = list2_node.next.as_ref();
    //         curr = curr.next.as_mut().unwrap();
    //     }

    //     dummy_head.next
    // }

    // pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     match (list1, list2) {
    //         (None, None) => None,
    //         (Some(l1), None) => Some(l1),
    //         (None, Some(l2)) => Some(l2),
    //         (Some(l1), Some(l2)) => {
    //             if l1.val < l2.val {
    //                 return Some(Box::new(ListNode {
    //                     val:l1.val, 
    //                     next: Solution::merge_two_lists(l1.next, Some(l2))
    //                 }))
    //             } else {
    //                 return Some(Box::new(ListNode {
    //                     val:l2.val, 
    //                     next: Solution::merge_two_lists(Some(l1), l2.next)
    //                 }))
    //             }
    //         }
    //     }
    // }

    // ref: https://leetcode.com/problems/merge-two-sorted-lists/solutions/2947855/simple-and-efficient-rust-8-liner/
    // pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     let mut curr = &mut list1; // calculate base on 1st node of list1 (it can be another one)

    //     while list2.is_some() { // if list2 is None, end the compare and swap
    //         if curr.is_none() || list2.as_ref()?.val < curr.as_ref()?.val { // continue to swap the tails of these two
    //             std::mem::swap(curr, &mut list2);
    //         }
    //         curr = &mut curr.as_mut()?.next; // move ptr to the next
    //     }

    //     list1
    // }

    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = Box::new(ListNode::new(0));
        let mut curr = &mut dummy_head;

        while list1.is_some() && list2.is_some() {
            let val1 = list1.as_ref().unwrap().val;
            let val2 = list2.as_ref().unwrap().val;

            if val1 < val2 {
                let mut l1 = list1.take().unwrap();
                list1 = l1.next.take();
                curr.next = Some(l1);
            } else {
                let mut l2 = list2.take().unwrap();
                list2 = l2.next.take();
                curr.next = Some(l2);
            }
            curr = curr.next.as_mut().unwrap();
            
        }
        curr.next = if list1.is_some() { list1 } else { list2 };

        dummy_head.next
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    use crate::util::linked_list::to_list;

    #[test]
    fn tets_21() {
        assert_eq!(
            Solution::merge_two_lists(to_list(vec![1,2,4]), to_list(vec![1,3,4])),
            to_list(vec![1,1,2,3,4,4])
        );

        assert_eq!(
            Solution::merge_two_lists(to_list(vec![]), to_list(vec![])),
            to_list(vec![])
        );

        assert_eq!(
            Solution::merge_two_lists(to_list(vec![]), to_list(vec![0])),
            to_list(vec![0])
        )
    }
}