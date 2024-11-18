use std::mem::swap;

pub struct Solution;

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        // 從最後一個往前比較，如果大於前一個則 swap
        //    若觸發 swap 則將後端將較小值依序往前推至 swap 處
        // 如果小於則往前繼續比較
        //    若一直沒觸發 swap，則以最小排列處理

        let last = nums.len();
        let mut trigger = None;

        for n in (1..last).rev() {
            if nums[n] > nums[n-1] {
                (nums[n], nums[n-1]) = (nums[n-1], nums[n]);
                trigger = Some(n);
                break;
            }
            println!("{:?}, {}", nums, n);
        }
        if let Some(trigger) = trigger {
            nums[trigger..].sort();
        } else {
            nums.sort();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_31 () {
        let mut vec1 = vec![1, 2, 3, 4, 5];
        Solution::next_permutation(&mut vec1);
        assert_eq!(vec1, vec![1, 2, 3, 5, 4]);

        let mut vec2 = vec![5, 4, 3, 2, 1];
        Solution::next_permutation(&mut vec2);
        assert_eq!(vec2, vec![1, 2, 3, 4, 5]);

        let mut vec2 = vec![1, 5, 2, 3, 4];
        Solution::next_permutation(&mut vec2);
        assert_eq!(vec2, vec![1, 2, 3, 4, 5]);
    }
}