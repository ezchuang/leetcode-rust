use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let value_arr = vec![
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ];
        let value_map: HashMap<_, _> = value_arr.into_iter().collect();
        let chars: Vec<char> = s.chars().collect();
        let mut res = 0;

        let mut i= 0;
        while i < s.len() {
            let value_1 = value_map[&chars[i]];

            if i + 1 < s.len() && value_1 < value_map[&chars[i + 1]] {
                res += value_map[&chars[i + 1]] - value_1;
                i += 2;
            } else {
                res += value_1;
                i += 1;
            }
        }

        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_13() {
        assert_eq!(Solution::roman_to_int("III".to_string()), 3);
        assert_eq!(Solution::roman_to_int("LVIII".to_string()), 58);
        assert_eq!(Solution::roman_to_int("MCMXCIV".to_string()), 1994);
    }
}