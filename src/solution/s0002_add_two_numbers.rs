use crate::util::linked_list::{to_list, ListNode};

pub struct Solution {}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // shadowing
        let (mut l1, mut l2) = (l1.as_deref(), l2.as_deref());

        // init
        let mut head = Some(Box::new(ListNode::new(0)));
        let mut curr = head.as_mut();
        let mut carry = 0;

        // main calculation
        while l1.is_some() || l2.is_some() || carry != 0 {
            let a = l1.map_or(0, |x| x.val);
            let b = l2.map_or(0, |x| x.val);

            let mut sum = a + b + carry;
            carry = sum / 10;
            sum = sum % 10;

            if let Some(x) = curr {
                x.next = Some(Box::new(ListNode::new(sum)));
                curr = x.next.as_mut();
            }

            l1 = l1.and_then(|node| node.next.as_deref());
            l2 = l2.and_then(|node| node.next.as_deref());
        }

        head.unwrap().next
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2() {
        assert_eq!(
            Solution::add_two_numbers(to_list(vec![2, 4, 3]), to_list(vec![5, 6, 4])),
            to_list(vec![7, 0, 8])
        );

        assert_eq!(
            Solution::add_two_numbers(to_list(vec![9, 9, 9, 9]), to_list(vec![9, 9, 9, 9, 9, 9])),
            to_list(vec![8, 9, 9, 9, 0, 0, 1])
        );

        assert_eq!(
            Solution::add_two_numbers(to_list(vec![0]), to_list(vec![0])),
            to_list(vec![0])
        )
    }
}