package Go

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {

	closestSum := 1 << 31

	sort.Ints(nums)

	i := 0
	for i < len(nums)-2 {

		start := i + 1
		end := len(nums) - 1

		for start < end {
			curSum := nums[i] + nums[start] + nums[end]

			diff := int(math.Abs(float64(target - curSum)))

			if diff == 0 {
				return curSum
			}
			if diff < int(math.Abs(float64(target-closestSum))) {
				closestSum = curSum
			}
			if curSum < target {
				start += 1
			} else {
				end -= 1
			}
		}

		i += 1
	}
	return closestSum

}
