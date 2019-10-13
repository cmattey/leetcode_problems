# Time: init: O(N), pick: O(logN)
# Space: O(N)

class Solution:
    import random
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        rect_areas = []
        for rect in rects:
            rect_areas.append(self.get_area(rect))

        self.sum_areas = sum(rect_areas)

        self.cum_sum = [rect_areas[0]]
        for i in range(1,len(rect_areas)):
            self.cum_sum.append(self.cum_sum[i-1]+rect_areas[i])

    def get_area(self,rect):
        x1,y1,x2,y2 = rect
        return abs(y2-y1+1)*abs(x2-x1+1)


    def pick(self) -> List[int]:
        rand_num = random.randint(0,self.sum_areas)

        rect_index = -1
        # for index,sum in enumerate(self.cum_sum): # Can do binary search here to reduce to O(logN)
        #     if sum>=rand_num:
        #         rect_index = index
        #         break

        low = 0
        high = len(self.cum_sum)-1

        while low<=high:
            mid = (low+high)//2
            if self.cum_sum[mid]==rand_num:
                rect_index = mid
                break
            elif self.cum_sum[mid]>rand_num:
                high = mid-1
            else:
                low = mid+1

        if rect_index==-1:
            rect_index = low

        rect = self.rects[rect_index]
        min_x = min(rect[0],rect[2])
        max_x = max(rect[0],rect[2])
        min_y = min(rect[1],rect[3])
        max_y = max(rect[1],rect[3])
        return [random.randint(min_x,max_x),random.randint(min_y,max_y)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
