# 11. Container With Most Water
# Time: O(len(height))
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        max_area = 0

        while left<right:
            area = min(height[left],height[right])*(right-left)

            if area>max_area:
                max_area = area

            if height[left]>height[right]:
                right-=1
            else:
                left+=1

        return max_area
