pub struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let mut parentheses_stack: Vec<char> = Vec::new();
        let mut res = true;

        for n in 0..chars.len() {
            match chars[n] {
                '(' | '{' | '[' => parentheses_stack.push(chars[n]),
                ')'  => res = parentheses_stack.pop() == Some('('),
                ']'  => res = parentheses_stack.pop() == Some('['),
                '}'  => res = parentheses_stack.pop() == Some('{'),
                _ => (),
            }
            if res == false {
                return false;
            }
        }

        parentheses_stack.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_20() {
        assert_eq!(Solution::is_valid("()".to_string()), true);
        assert_eq!(Solution::is_valid("()[]{}".to_string()), true);
        assert_eq!(Solution::is_valid("(]".to_string()), false);
        assert_eq!(Solution::is_valid("([])".to_string()), true);
    }

}