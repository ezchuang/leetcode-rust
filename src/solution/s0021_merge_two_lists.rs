pub struct Solution {}

use crate::util::linked_list::ListNode;

impl Solution {
    // try not to mutate parameters
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut list1, mut list2) = (list1.as_ref(), list2.as_ref());
        let mut dummy_head = Box::new(ListNode::new(0));
        let mut curr = &mut dummy_head;

        while let (Some(list1_node), Some(list2_node)) = (list1, list2) {
            if list1_node.val <= list2_node.val {
                curr.next = Some(Box::new(ListNode::new(list1_node.val)));
                list1 = list1_node.next.as_ref();
            } else {
                curr.next = Some(Box::new(ListNode::new(list2_node.val)));
                list2 = list2_node.next.as_ref();
            }
            curr = curr.next.as_mut().unwrap();
        }

        while let Some(list1_node) = list1 {
            curr.next = Some(Box::new(ListNode::new(list1_node.val)));
            list1 = list1_node.next.as_ref();
            curr = curr.next.as_mut().unwrap();
        }

        while let Some(list2_node) = list2 {
            curr.next = Some(Box::new(ListNode::new(list2_node.val)));
            list2 = list2_node.next.as_ref();
            curr = curr.next.as_mut().unwrap();
        }

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