# Time: O(nlogn)
# Space: O(1), excluding car_info else: O(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Sort based on distance after zipping with speed.
        Calculate time to target, and use that to calculate fleet.
        """

        car_info = sorted(zip(position,speed), reverse=True)
        # reverse, because we want to calculate starting from cars closest
        # to the target, i.e. with highest position.

        print(car_info)
        prev_time = -1
        fleet = 0

        for pos, sp in car_info:
            time = (target-pos)/sp

            if time>prev_time:
                fleet+=1
                prev_time = time

        return fleet
