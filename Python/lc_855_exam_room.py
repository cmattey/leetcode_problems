# Time: init: O(1), seat: O(N), leave: O(1)

class ExamRoom:
    """
    TLE Solution
    """
    def __init__(self, N: int):
        self.N = N
        self.arr = [None]*N

    def seat(self) -> int:

        N = self.N

        if all(val is None for val in self.arr):
            self.arr[0] = 1
            return 0

        left = [float('inf')]*N
        right = [float('inf')]*N

        prev_seat = None

        for i in range(N):
            if self.arr[i]==1:
                prev_seat = i
                left[i] = 0
            else:
                if prev_seat is not None:
                    left[i] = i-prev_seat

        prev_seat = None
        for i in range(N-1,-1,-1):
            if self.arr[i]==1:
                prev_seat = i
                right[i] = 0
            else:
                if prev_seat is not None:
                    right[i] = prev_seat - i

        shortest_dist = [None]*N
        max_dist = float('-inf')
        min_index = None

        # print("left",left)
        # print("right",right)
        for i in range(N):
            shortest_dist[i] = min(left[i], right[i])

            if shortest_dist[i]>max_dist:
                max_dist = shortest_dist[i]
                min_index = i

        self.arr[min_index] = 1
        return min_index

    def leave(self, p: int) -> None:
        self.arr[p] = 0
        return None



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
