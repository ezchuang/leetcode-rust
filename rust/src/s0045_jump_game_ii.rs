pub struct Solution;

impl Solution {
    // pub fn jump(nums: Vec<i32>) -> i32 {
    //     let last_index = (nums.len() - 1) as usize;
    //     if last_index == 0 {
    //         return 0;
    //     }

    //     let mut curr_val = nums[0];
    //     let mut res = 1;
    //     let mut l= 0;

    //     while (l + curr_val as usize) < last_index {
    //         let val_l = nums[l] as usize;

    //         match nums[l + 1..l + val_l + 1].iter().enumerate().max_by_key(|&(i, &val)| i + val as usize) {
    //             Some((index, &max)) => {
    //                 res += 1;
    //                 l = l + index + 1;
    //                 curr_val = max;
    //             }
    //             None => {
    //                 break;
    //             },
    //         }
    //     }

    //     res
    // }

    pub fn jump(nums: Vec<i32>) -> i32 {
        let last_index = nums.len() - 1;
        let mut cnt: i32 = 0;
        let mut prev_reach: usize = 0;
        let mut curr_max: usize = nums[0] as usize;

        for i in 1..last_index + 1 {
            if curr_max >= last_index {
                cnt += 1;
                break;
            }

            if i > prev_reach {
                cnt += 1;
                prev_reach = curr_max;
            }

            curr_max = if i + nums[i] as usize > curr_max { i + nums[i] as usize } else { curr_max }
        }

        cnt
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_45() {
        assert_eq!(Solution::jump(vec![2,3,1,1,4]), 2);
        assert_eq!(Solution::jump(vec![2,3,0,1,4]), 2);
        assert_eq!(Solution::jump(vec![2,2,0,1,4]), 3);
        assert_eq!(Solution::jump(vec![0]), 0);
        assert_eq!(Solution::jump(vec![2,1]), 1);
        assert_eq!(Solution::jump(vec![1]), 0);
    }
}