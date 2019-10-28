# Time: O(log(sum_weight)*len(weights)) <-check
# Space: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        Binary Search approach
        inspired by: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/346505/Binary-classification-Python.-Detailed-explanation-Turtle-Code
        """

        min_cap = max(weights)  # If I had inf days
        max_cap = sum(weights)  # If I had 1 day, these are the limits to the capacity

        while min_cap<max_cap:

            mid = (min_cap+max_cap)//2  # my guess for min cap of a day

            cur_cap = 0
            num_days = 1

            for weight in weights:
                cur_cap+=weight

                if cur_cap>mid:
                    # print(cur_cap-weight)
                    cur_cap = weight
                    num_days+=1

            if num_days>D:
                min_cap = mid+1
            else:
                max_cap = mid

        return min_cap
            
