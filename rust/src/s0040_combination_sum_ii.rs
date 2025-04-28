pub struct Solution;

impl Solution {
    // pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
    //     // sort 後，用 backtrace 窮舉，並檢查是否重複
    //     let mut res:Vec<Vec<i32>> = Vec::new();
    //     let mut sorted_candidates: Vec<i32> = candidates.clone();
    //     sorted_candidates.sort_unstable();
    //     Self::backtrack(&sorted_candidates, target, &mut Vec::new(), &mut res);

    //     res
    // }

    // fn backtrack(sub_slice: &[i32], remain: i32, combination: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
    //     if remain == 0 {
    //         res.push(combination.clone());
    //         return;
    //     }

    //     for i in 0..sub_slice.len() {
    //         if i > 0 && sub_slice[i] == sub_slice[i - 1] {
    //             continue;
    //         }

    //         if sub_slice[i] > remain {
    //             break;
    //         }

    //         combination.push(sub_slice[i]);
    //         if i < sub_slice.len() - 1 {
    //             Self::backtrack(&sub_slice[i + 1..], remain - sub_slice[i], combination, res);
    //         } else {
    //             Self::backtrack(&[], remain - sub_slice[i], combination, res);
    //         }
    //         combination.pop();
    //     }
    // }

    // https://leetcode.com/problems/combination-sum-ii/solutions/4819825/o-2-n-0-ms-beats-100-java-c-python-go-rust-javascript/
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res:Vec<Vec<i32>> = Vec::new();
        let mut sorted_candidates: Vec<i32> = candidates.clone();
        sorted_candidates.sort_unstable();
        Self::backtrack(&sorted_candidates, target, 0, &mut Vec::new(), &mut res);

        res
    }

    fn backtrack(candidates: &[i32], remain: i32, start: usize, combination: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if remain == 0 {
            res.push(combination.clone());
            return;
        }

        for i in start..candidates.len() {
            if i > start && candidates[i] == candidates[i - 1] {
                continue;
            }

            if candidates[i] > remain {
                break;
            }

            combination.push(candidates[i]);
            Self::backtrack(candidates, remain - candidates[i], i + 1, combination, res);
            combination.pop();
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_40() {
        assert_eq!(Solution::combination_sum2(vec![10,1,2,7,6,1,5], 8), vec![vec![1,1,6],vec![1,2,5],vec![1,7],vec![2,6]]);
        assert_eq!(Solution::combination_sum2(vec![2,5,2,1,2], 5), [vec![1,2,2],vec![5]]);
        assert_eq!(Solution::combination_sum2(vec![9, 9, 9], 3), Vec::<Vec<i32>>::new());
        assert_eq!(Solution::combination_sum2(vec![1,1,1,1,1,1,1,2,1], 3), vec![vec![1,1,1], vec![1,2]]);
    }
}