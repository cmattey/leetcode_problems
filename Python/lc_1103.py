# 1103. Distribute Candies to People
# Weekly Contest 143
# To be Refactored
# Time: O(candies)
# Space: O(num_people)
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        row = [0]*num_people

        cur_index = 0
        total_given = 0
        prev_given = 0
        candies_left = candies

        while candies_left>0:
            if row[0] == 0:
                total_given = 1
                row[0]=1
                candies_left-=1
                cur_index+=1
                prev_given = 1
            elif total_given + prev_given +1 <= candies:
                total_given +=prev_given + 1
                row[cur_index] += prev_given + 1
                cur_index+=1
                candies_left-=prev_given + 1
                prev_given+=1
            elif total_given + prev_given + 1 > candies:
                row[cur_index] += candies-total_given
                break

            if cur_index==num_people:
                cur_index = 0

        return row
