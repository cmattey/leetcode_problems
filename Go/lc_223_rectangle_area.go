pacakge Go
// O(1)
func computeArea(A int, B int, C int, D int, E int, F int, G int, H int) int {
    
    width, height := 0,0
    
    if E<=C && E>=A{
        width = min(C, G) - E
    } else if A>=E && A<=G{
        width =  min(C, G) - A
    }
    
    if H >=B && H<=D {
        height = H - max(B, F)
    } else if D>=F && D<=H{
        height = D - max(B, F)
    }
    
    
    area1 := (D-B)*(C-A)
    area2 := (H-F)*(G-E)
    
    return area1+area2 - (width*height)
}

func max(a, b int)int{
    if a<b{
        return b
    }
    return a
}

func min(a, b int)int{
    if a<b{
        return a
    }
    return b
}