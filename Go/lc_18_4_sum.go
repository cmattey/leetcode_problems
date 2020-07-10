package Go

import (
	"sort"
)

func fourSum(nums []int, target int) [][]int {

	sort.Ints(nums)

	sol := [][]int{}

	i := 0

	for i < len(nums)-3 {
		partSols := threeSumHelper(nums[i+1:], target-nums[i])
		for _, partSol := range partSols {
			partSol = append(partSol, nums[i])
			sol = append(sol, partSol)
		}
		i++
		for nums[i] == nums[i-1] && i < len(nums)-3 {
			i++
		}
	}
	return sol
}

func threeSumHelper(nums []int, target int) [][]int {

	sort.Ints(nums)

	sol := [][]int{}
	i := 0
	// fmt.Println(nums)
	for i < len(nums)-2 {
		start := i + 1
		end := len(nums) - 1
		for start < end {

			if nums[i]+nums[start]+nums[end] == target {
				sol = append(sol, []int{nums[i], nums[start], nums[end]})
				end--
				for nums[end] == nums[end+1] && start < end {
					end--
				}

				start++
				for nums[start] == nums[start-1] && start < end {
					start++
				}
			} else if nums[i]+nums[start]+nums[end] > target {
				end--
			} else {
				start++
			}
		}

		i++
		for nums[i] == nums[i-1] && i < len(nums)-2 {
			i++
		}
	}

	return sol
}
