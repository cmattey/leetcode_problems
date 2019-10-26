# Time: O(n)
# Space: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Keep an index stack, and a height stack.
        manipulate them properly.
        push if element larger than top, else pop, and calculate area.
        When we pop, we are essentially calculating the area of the rectangle with the previous height.
        The position needs to be taken care of accordingly.
        Can also do in O(n^2), with nested loops to compare min_height, between pairs of i and j, with j>i.
        """


        position = []
        height = []

        max_area = 0
        for pos, h in enumerate(heights):
            if len(height)==0:
                position.append(pos)
                height.append(h)

            else:

                if height and h>height[-1]:
                    position.append(pos)
                    height.append(h)

                else:
                    while height and position and h<height[-1]:
                        prev_height = height.pop()
                        prev_pos = position.pop()
                        max_area = max(max_area, prev_height*(pos-prev_pos))

                    if height and h>height[-1]:     # Notice that we append the prev_pos
                        position.append(prev_pos)
                        height.append(h)
                    if not height:
                        position.append(prev_pos)
                        height.append(h)


        while position:
            prev_height = height.pop()
            prev_pos= position.pop()
            max_area = max(max_area, prev_height*(len(heights)-prev_pos))

        return max_area
