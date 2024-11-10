
use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums_map = HashMap::new();
        
        for (index, num) in nums.iter().enumerate(){
            let complement = target - num; // subtract to avoid overflow

            if let Some(sub_index) = nums_map.get(&complement){
                return vec![*sub_index, index as i32]
            }

            nums_map.insert(num, index as i32);
        }

        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(vec![0, 1], Solution::two_sum(vec![2, 7, 11, 15], 9));
        assert_eq!(vec![1, 2], Solution::two_sum(vec![3, 2, 4], 6));
    }
}