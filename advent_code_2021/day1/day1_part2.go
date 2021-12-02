package main

import (
"fmt"
"bufio"
"os"
"strconv"
)


func main() {

nums := readNums("day1_input.txt")

var incr int
for i := range nums{
	if i==0 || i==1 || i==2{
		continue
	}else{
		if nums[i]>nums[i-3]{
			incr++
		}
	}
}

fmt.Println(incr)
}

func readNums(filename string)[]int{
	var nums []int
	
file,_ := os.Open(filename)

scanner := bufio.NewScanner(file)

for scanner.Scan(){
i, _ := strconv.Atoi(scanner.Text())
nums = append(nums, i)
}

return nums
}
