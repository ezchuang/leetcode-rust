package pkg

import "unicode"

// 125. Valid Palindrome
// two pointer
// check the left and right character is letter(or Number) or not.
// if the answer is no. push the pointer to the next.
// check if the valid char on index left and right is the same unicode.
// if no, return false.
// if yes, to the next turn.
func isPalindrome(s string) bool {
	var l, r int = 0, len(s) - 1 //
	for l <= r {
		if !unicode.IsLetter(rune(s[l])) && !unicode.IsNumber(rune(s[l])) {
			l++
		} else if !unicode.IsLetter(rune(s[r])) && !unicode.IsNumber(rune(s[r])) {
			r--
		} else if unicode.ToLower(rune(s[l])) != unicode.ToLower(rune(s[r])) {
			return false
		} else {
			l++
			r--
		}
	}
	return true
}
