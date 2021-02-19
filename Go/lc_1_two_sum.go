
package go

// Time: O(n)
// Space: O(n)

func twoSum(nums []int, target int) []int {

	imap := make(map[int]int)

	for index1, val1 := range nums {
		if index2, ok := imap[target-val1]; ok {
			return []int{index2, index1}
		}

		imap[val1] = index1
	}

	return []int{-1, -1}
}
