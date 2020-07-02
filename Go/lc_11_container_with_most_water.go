func maxArea(height []int) int {
    
    max := 0
    start := 0
    end := len(height)-1
    
    for start < end{
        max = Max(max, (end-start)*Min(height[start],height[end]))
        if height[start] < height[end]{
            start+=1
        }else{
            end-=1
        }
    }
    
    return max
    
}

func Max(a int, b int) int{
    if a>b{
        return a
    }
    return b
}
                  
func Min(a int, b int) int{
    if a<b{
        return a
  }
    return b
}