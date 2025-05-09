package pkg

import (
	"sort"
	"strings"
)

// solution description:
//
//	two pointer
//	rearrange each char in the word in strs, and put it into a map(dict)
//	key of the map is rearranged word, and the value of the map is array of origin word.
//	return all the values of the map
func groupAnagrams(strs []string) [][]string {
	res := make([][]string, 0)
	wordMap := make(map[string][]string)

	for _, word := range strs {
		chars := strings.Split(word, "")
		sort.Strings(chars)
		sortedWord := strings.Join(chars, "")

		wordMap[sortedWord] = append(wordMap[sortedWord], word)
	}

	for _, v := range wordMap {
		res = append(res, v)
	}

	return res
}
