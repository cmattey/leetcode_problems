# Nov 19th '19
# Time: O(n*log(sum_wts)), where n = len(weights), sum_wts = sum(weights)
# Space: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        if D==len(weights), min_weight_capacity = max(weights)
        if D==1, min_weight_capacity = sum(weights)

        we have a range for the min_capacity, use binary search to figure out min_cap, by calculating number of days required to transport, and comparing it with D to adjust the bounds of the search space.

        Errichto Binary Search
        """

        left = max(weights)
        right= sum(weights)

        # print(left, right)
        while left<=right:

            guess_cap= (left+right)//2
            guess_days = 1
            cur_weight = 0
            for w in weights:
                cur_weight+=w

                if cur_weight>guess_cap:
                    cur_weight = w
                    guess_days+=1

            # print("cap, days", guess_cap, guess_days)
            if guess_days<=D: # Can ship within D days, and not exactly D days
                ans = guess_cap
                right = guess_cap-1
            else: # guess_days>D
                left = guess_cap+1

        return ans

# Nov 18th '19
# Time: O(n*log(sum_wts)), where n = len(weights), sum_wts = sum(weights) or search range viz sum(weights)-min(weights) to be more precise
# Space: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        if D==len(weights), min_weight_capacity = max(weights)
        if D==1, min_weight_capacity = sum(weights)

        we have a range for the min_capacity, use binary search to figure out min_cap, by calculating number of days required to transport, and comparing it with D to adjust the bounds of the search space.
        """

        left = max(weights)
        right= sum(weights)

        while left<right:

            guess_cap= (left+right)//2
            guess_days = 1
            cur_weight = 0
            for w in weights:
                cur_weight+=w

                if cur_weight>guess_cap:
                    cur_weight = w
                    guess_days+=1

            if guess_days>D:
                left = guess_cap+1
            else:
                right = guess_cap

        return right

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
