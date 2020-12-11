package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
)

// NumSet is a set data structure that holds integers
// Only implementing functions necessary to solve this problem
type NumSet struct {
	items map[int]bool
}

func (s *NumSet) Add(i int) *NumSet {
	if s.items == nil {
		s.items = make(map[int]bool)
	}
	_, ok := s.items[i]
	if !ok {
		s.items[i] = true
	}
	return s
}

func (s1 *NumSet) Intersection(s2 *NumSet) *NumSet {

	s3 := NumSet{}
	s3.items = make(map[int]bool)

	for i := range s1.items {

		if _, ok := s2.items[i]; ok {
			s3.items[i] = true
		}
	}
	return &s3
}

func (s *NumSet) Size() int {
	return len(s.items)
}

func (s *NumSet) Reset() {
	s.items = make(map[int]bool)
	// s.items = nil
}

func main() {

	fmt.Println(solveDay6("Day6_input.txt"))
}

func solveDay6(filename string) int {

	strs := helpers.ReadStr((filename))

	curSet := NumSet{}
	ans := 0
	firstSet := true
	for i, st := range strs {

		if len(st) == 0 || i == len(strs)-1 {
			// fmt.Println(curSet.items)
			ans += curSet.Size()
			curSet.Reset()
			firstSet = true
		} else {
			tempSet := NumSet{}
			for _, ch := range st {
				tempSet.Add(int(ch))
			}
			if firstSet {
				curSet = tempSet
				firstSet = false
			} else {
				curSet = *curSet.Intersection(&tempSet)
			}
		}
	}

	return ans
}
