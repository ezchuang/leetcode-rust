pub struct Solution;

impl Solution {
    // pub fn next_permutation(nums: &mut Vec<i32>) {
        // 從最後一個往前比較，如果大於前一個則觸發 swap
        //    將觸發處 (當前 index) 往後看 "大於對比值 (index-1) 的最小值" 跟 "對比值" swap
        //    若有觸發 swap，則將觸發點 (index) 往後的 arr 重新排序
        // 如果小於，則往前繼續比較
        //    若一直沒觸發 swap，則以最小排列處理(反序)

    //     let last = nums.len() - 1;
    //     let (mut n, mut m) = (last, last);

    //     while n >= 1 && nums[n - 1] >= nums[n] {
    //         n -= 1;
    //     }

    //     while n >= 1 && nums[n - 1] >= nums[m] {
    //         m -= 1;
    //     }

    //     if n > 0 {
    //         nums.swap(n - 1, m);
    //         nums[n..].sort();
    //     } else {
    //         nums.reverse();
    //     }
    // }

    pub fn next_permutation(nums: &mut Vec<i32>) {
        let last = nums.len() - 1;
        let (mut n, mut m) = (last, last);

        while n >= 1 && nums[n - 1] >= nums[n] { n -= 1; }

        if n > 0 {
            while n >= 1 && nums[n - 1] >= nums[m] { m -= 1; }

            nums.swap(n - 1, m);
        }

        nums[n..].reverse();
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
        assert_eq!(vec2, vec![1, 5, 2, 4, 3]);

        let mut vec2 = vec![1, 5, 4, 3, 2];
        Solution::next_permutation(&mut vec2);
        assert_eq!(vec2, vec![2, 1, 3, 4, 5]);
    }
}