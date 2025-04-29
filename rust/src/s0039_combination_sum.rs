pub struct Solution;

impl Solution {
    pub fn combination_sum(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut temp_res: Vec<i32> = Vec::new();

        candidates.sort();

        fn sub_fn(candidates: &[i32], target: i32, temp_res: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            if target == 0 {
                res.push(temp_res.clone());
                return;
            }

            let length = candidates.len();
            if target < 0 || length <= 0 {
                return;
            }

            for i in 0..length {
                temp_res.push(candidates[i]);
                sub_fn(&candidates[i..], target - candidates[i], temp_res, res);
                temp_res.pop();
            }
        }

        sub_fn(&candidates, target, &mut temp_res, &mut res);

        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_39() {
        assert_eq!(
            Solution::combination_sum(vec![2, 3, 6, 7], 7), 
            vec![vec![2, 2, 3], vec![7]]
        );
        assert_eq!(
            Solution::combination_sum(vec![2, 3, 5], 8), 
            vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]]
        );
        assert_eq!(
            Solution::combination_sum(vec![2], 1), 
            Vec::<Vec<i32>>::new()
        );
    }
}