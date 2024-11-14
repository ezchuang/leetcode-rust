pub struct Solution();

impl Solution {
    // compare with char iterator
    // pub fn is_palindrome(x: i32) -> bool {
    //     // early return
    //     if x < 0 {
    //         return false;
    //     }

    //     // init
    //     let x_string = x.to_string();
    //     let (mut l, mut r) = (0, x_string.len() - 1);

    //     // main
    //     while l < r {
    //         if x_string.chars().nth(l) != x_string.chars().nth(r) {
    //             return false;
    //         }

    //         l += 1;
    //         r -= 1;
    //     }

    //     true
    // }

    // compare with string as bytes
    // pub fn is_palindrome(x: i32) -> bool {
    //     // early return
    //     if x < 0 {
    //         return false;
    //     }

    //     // convert integer to string as bytes
    //     let x_string = x.to_string(); // Save the temporary string to extend its lifetime
    //     let x_bytes = x_string.as_bytes(); // Then retrieve a byte reference to avoid borrowing a temporary value
    //     let (mut l, mut r) = (0, x_bytes.len() - 1);

    //     // main
    //     while l < r {
    //         if x_bytes[l] != x_bytes[r] {
    //             return false;
    //         }
    //         l += 1;
    //         r -= 1;
    //     }

    //     true
    // }

    // compare with reverse x
    pub fn is_palindrome(x: i32) -> bool {
        // early return
        if x < 0 {
            return false;
        }

        // init
        let mut num = x;
        let mut rev = 0;

        while num != 0 {
            rev = rev * 10 + num % 10;
            num /= 10;
        }

        return x == rev;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_9() {
        assert_eq!(Solution::is_palindrome(121), true);
        assert_eq!(Solution::is_palindrome(-121), false);
        assert_eq!(Solution::is_palindrome(10), false);
        assert_eq!(Solution::is_palindrome(0), true);
    }
}