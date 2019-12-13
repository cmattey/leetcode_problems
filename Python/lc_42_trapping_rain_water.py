# Nov 26th '19
# Time: O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Constant Space Solution
        Key idea is to measure the water chunk on top of each column,
        using the max-height of column to it's left and right.
        """
        total_water = 0



        left = 0
        right = len(height)-1

        left_max = float('-inf')
        right_max = float('-inf'
                         )
        while left<right:

            if height[right]>height[left]:

                if height[left]>left_max:
                    left_max = height[left]
                else:
                    total_water+=left_max-height[left]
                left+=1

            else:

                if height[right]>right_max:
                    right_max = height[right]
                else:
                    total_water+=right_max-height[right]

                right-=1

        return total_water

# Time: O(n)
# Space: O(n) -> Can be reduced to O(1), using two pointers

class Solution:
    def trap(self, height: List[int]) -> int:


        left_max = float('-inf')
        right_max = float('-inf')

        left_arr = [0]*len(height)
        right_arr = [0]*len(height)

        for i in range(len(height)):
            if height[i]>left_max:
                left_max = height[i]
                left_arr[i] = left_max
            elif height[i]<=left_max:
                left_arr[i] = left_max

        for i in reversed(range(len(height))):
            if height[i]>right_max:
                right_max = height[i]
                right_arr[i] = right_max
            else:
                right_arr[i] = right_max

        total_water = 0
        for index in range(1,len(left_arr)-1):
            overhead_water = min(left_arr[index], right_arr[index])-height[index]
            total_water+=overhead_water

        return total_water
