package Go

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {

	sort.Ints(nums)

	sol := [][]int{}
	i := 0
	fmt.Println(nums)
	for i < len(nums)-2 {
		start := i + 1
		end := len(nums) - 1
		for start < end {

			if nums[i]+nums[start]+nums[end] == 0 {
				sol = append(sol, []int{nums[i], nums[start], nums[end]})
				end -= 1
				for nums[end] == nums[end+1] && start < end {
					end -= 1
				}

				start += 1
				for nums[start] == nums[start-1] && start < end {
					start += 1
				}
			} else if nums[i]+nums[start]+nums[end] > 0 {
				end -= 1
			} else {
				start += 1
			}
		}

		i += 1
		for nums[i] == nums[i-1] && i < len(nums)-2 {
			i += 1
		}
	}

	return sol
}
