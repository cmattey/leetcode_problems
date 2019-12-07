# Time: p*log(max(piles))
# Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:


        left = 1
        right = max(piles)

        ans = -1
        while left<=right:

            guess_speed = (left+right)//2

            start_hours = 0
            eaten_so_far = 0

            for pile in piles:

                if guess_speed>=pile:
                    eaten_so_far+=pile
                    start_hours+=1
                elif guess_speed<pile:
                    start_hours+=math.ceil(pile/guess_speed)

            if start_hours>H:
                left = guess_speed+1
            elif start_hours<=H:
                ans = guess_speed
                right = guess_speed-1

        return ans
