# 1109. Corporate Flight Bookings
# Weekly Contest 144
# Time: O(len(n))
# Space: O(n)
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        """
        Shorter solution:
        """

        res = [0]*(n+1)
        for i,j,k in bookings:
            res[i-1]+=k
            res[j]-=k

        for i in range(1,n):
            res[i]+=res[i-1]

        return res[:-1]


        """
        Longer Solution
        """


        result = [{} for _ in range(n)]

        for booking in bookings:
            i,j,k = booking[0],booking[1],booking[2]

            if 'start' in result[i-1]:
                result[i-1]['start']+=k
            else:
                result[i-1]['start']=k
            if 'end' in result[j-1]:
                result[j-1]['end']+=k
            else:
                result[j-1]['end']=k

        adder = 0
        seats = [0]*n
        for index,flight in enumerate(result):
            if 'start' in flight:
                adder+=flight['start']

            seats[index]+=adder

            if 'end' in flight:
                adder-=flight['end']


        return seats
