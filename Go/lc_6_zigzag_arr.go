// Time: O(n)
// Space: O(1)
// Can be done with more concise code by creating a matrix of rows,
// which takes O(n) extra space. The below solution is constant space.

import(
    "strings"
)
func convert(s string, numRows int) string {

    if numRows == 1 || numRows>=len(s){
        return s
    }

    var o []string

    cur_row := 0
    cur_index := 0
    up := false

    for len(o)<len(s) {

        if up{
            o = append(o, string(s[cur_index]))
            rem_rows := cur_row
            next_index := cur_index + (2*rem_rows)

            if next_index <len(s){
                cur_index = next_index
                if cur_row!=numRows-1{
                    up = !up
                }
            }else{
                cur_row += 1
                cur_index = cur_row
                if cur_row!=numRows-1{
                    up = !up
                }
            }

        }else{
            o = append(o, string(s[cur_index]))
            rem_rows := numRows - cur_row - 1
            next_index := cur_index+(rem_rows*2)

            if next_index < len(s){
                cur_index = next_index
                if cur_row!=0{
                    up = !up
                }
            }else{
                cur_row += 1
                cur_index = cur_row
                if cur_row==numRows-1{
                    up = !up
                }
            }
        }
    }

    output := strings.Join(o,"")
    return output
}
