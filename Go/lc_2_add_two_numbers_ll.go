// Time: O(n)
// Space: O(n),can reduce to O(1), by reusing input linked list
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    sum:= 0

    new_list := &ListNode{0, nil}
    new_ptr := new_list

    for l1!=nil || l2!=nil {

        if l1!=nil{
            sum+=l1.Val
            l1 = l1.Next
        }

        if l2!=nil{
            sum+=l2.Val
            l2 = l2.Next
        }

        new_ptr.Next = &ListNode{sum%10, nil}
        new_ptr = new_ptr.Next
        sum = sum/10
    }

    if sum!=0{
        new_ptr.Next = &ListNode{sum, nil}
    }
    return new_list.Next

}
