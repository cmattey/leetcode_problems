class SnapshotArray:
    """
    Store updates only on set operation
    Time:
        init->  O(1)
        set->   O(1)
        snap->  O(1)
        get->   O(log(set calls for that index)) worse case: O(log(snaps))
    Space:
        O(sets called + length)
    """
    def __init__(self, length: int):
        self.arr = [[[0,0]] for _ in range(length)] # [snap_id, value]
#       Each element will be of form: [[0,0]] -> collections of snapid and value
#       After multiple snaps each element can look like: [[0,1],[1,1],[2,2]...]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        """
        extra steps to modify values within the same snap id.
        search if snapid already exists, and modify value
        """
        # target_arr = self.arr[index]

        if self.arr[index][-1][0]!=self.snap_id: # since snapid are added in increasing order only need to check latest value
            self.arr[index].append([self.snap_id, val])
        else:
            self.arr[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.arr)
        target_arr = self.arr[index]

        return self.search_snap_id(target_arr, snap_id)

    def search_snap_id(self, arr, snap_id):
        """
        search for snap_id, return corresponding value
        we are looking for the left_most snap_id that was recorded in a previous set operation
        similar to binary search for insertion index
        """

        left = 0
        right = len(arr)

        while left+1<right:

            mid = (left+right)//2
            if arr[mid][0]==snap_id:
                return arr[mid][1]
            elif arr[mid][0]>snap_id:
                right = mid
            else:
                left = mid

        return arr[left][1]

        """
        Alternate binary search approach: Errichto
        We are looking for largest value smaller than or equal to target

        left = 0
        right = len(arr)-1
        ans = -1
        while left<=right:

            mid = (left+right)//2
            if arr[mid][0]<=snap_id:
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return arr[ans][1]
        """

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

class SnapshotArray:
    """
    MLE solution, storing multiple copies of arr
    """
    def __init__(self, length: int):
        self.arr = [0]*length
        self.snap_map = {}
        self.snap_index = -1

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_index+=1
        self.snap_map[self.snap_index] = self.arr[:]
        return self.snap_index

    def get(self, index: int, snap_id: int) -> int:

        return self.snap_map[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
