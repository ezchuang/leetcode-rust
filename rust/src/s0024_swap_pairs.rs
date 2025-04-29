pub struct Solution {}

use crate::util::linked_list::ListNode;

impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match head {
            Some(mut n1) => {
                if let Some(mut n2) = n1.next.take() {
                    n1.next = Self::swap_pairs(n2.next.take());
                    n2.next = Some(n1);
                    Some(n2)
                } else {
                    Some(n1)
                }
            }
            None => None
        }
    }
}


#[cfg(test)]
mod tests {
    use crate::util::linked_list::to_list;
    use super::*;

    #[test]
    fn test_24() {
        assert_eq!(
            Solution::swap_pairs(to_list(vec![1, 2, 3, 4])),
            to_list(vec![2, 1, 4, 3])
        );
        assert_eq!(Solution::swap_pairs(to_list(vec![])), to_list(vec![]));
        assert_eq!(
            Solution::swap_pairs(to_list(vec![1, 2, 3])),
            to_list(vec![2, 1, 3])
        );
        assert_eq!(Solution::swap_pairs(to_list(vec![1])), to_list(vec![1]));
    }
}