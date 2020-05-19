// Time: O(logn)
// Space: O(1)
func isPalindrome(x int) bool {
    copy_x := x

    if x<0{
        return false
    }

    rev := 0

    for x>0{
        rev = rev*10 + x%10
        x = x/10
    }

    if rev==copy_x{
        return true
    }
    return false
}
