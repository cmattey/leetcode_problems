package Go

// Time: O(log(min(m,n)))
// Space: O(1)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

	m := len(nums1)
	n := len(nums2)
	left1, left2, right1, right2 := 0, 0, 0, 0
	if m > n {
		nums1, nums2 = nums2, nums1
		m, n = n, m
	}

	minPart1 := 0 // Part=Partition
	maxPart1 := m

	for minPart1 <= maxPart1 {
		part1 := int((minPart1 + maxPart1) / 2)
		part2 := int((m+n+1)/2) - part1

		// fmt.Println("Partition", part1, part2)

		if part1 == 0 {
			left1 = -1 * (1 << 31)
		} else {
			left1 = nums1[part1-1]
		}

		if part2 == 0 {
			left2 = -1 * (1 << 31)
		} else {
			left2 = nums2[part2-1]
		}

		if part1 == len(nums1) {
			right1 = 1 << 31
		} else {
			right1 = nums1[part1]
		}

		if part2 == len(nums2) {
			right2 = 1 << 31
		} else {
			right2 = nums2[part2]
		}

		if left1 > right2 {
			maxPart1 = part1 - 1
		} else if left2 > right1 {
			minPart1 = part1 + 1
		} else {
			if (m+n)%2 == 0 {
				return float64((Max(left1, left2) + Min(right1, right2))) / 2
			} else {
				return float64(Max(left1, left2))
			}
		}
	}
	return 0.0
}

// func Max(x, y int) int {
// 	if x > y {
// 		return x
// 	}
// 	return y
// }

// func Min(x, y int) int {
// 	if x > y {
// 		return y
// 	}
// 	return x
// }
