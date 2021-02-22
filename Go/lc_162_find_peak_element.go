package Go

// O(logn)
func findPeakElement(nums []int) int {

	return binSearch(0, len(nums)-1, nums)
}

func binSearch(left, right int, nums []int) int {

	if left >= right {
		return left
	}

	mid := int((left + right) / 2)

	if nums[mid] > nums[mid+1] {
		return binSearch(left, mid, nums)
	}

	return binSearch(mid+1, right, nums)
}
