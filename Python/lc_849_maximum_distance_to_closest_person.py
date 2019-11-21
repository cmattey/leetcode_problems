# Time: O(n)
# Space: O(n)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        left_arr = [float('inf')]*len(seats)
        right_arr = [float('inf')]*len(seats)

        for i in range(len(seats)):

            if seats[i]!=1 and i>0:
                left_arr[i] = left_arr[i-1]+1
            elif seats[i]==1:
                left_arr[i] = 0


        for i in range(len(seats)-1,-1,-1):

            if seats[i]!=1 and i<len(seats)-1:
                right_arr[i] = right_arr[i+1]+1
            elif seats[i]==1:
                right_arr[i] = 0

        max_dist = float('-inf')
        for i in range(len(seats)):
            max_dist = max(max_dist, min(left_arr[i], right_arr[i]))

        return max_dist

# Time: O(n)
# Spaec: O(n)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        max_dist = -1
        last_seat = '#'
        arr = [float('inf')]*len(seats)

        for index, seat in enumerate(seats):
            if seat:
                last_seat = index
                arr[index] = 0
            else:
                if last_seat=='#':
                    continue
                arr[index] = index-last_seat

        print(arr)
        last_seat = '#'
        for index in reversed(range(len(seats))):
            if seats[index]:
                last_seat = index
            else:
                if last_seat=='#':
                    continue
                arr[index] = min(arr[index],last_seat-index)

        return max(arr)
