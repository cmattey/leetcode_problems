# Time: O(logn + k)
# Space: O(k)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        The question can be thought of as finding a sub-array of the given arr, around the closest element to x.
        Find x's insertion index in the array, and retrieve elements from around it.
        """

        if x<arr[0]:
            return arr[:k]
        elif x>arr[-1]:
            return arr[len(arr)-k:]

        index = self.findInsertionIndex(arr, x)

#         we k elements to left of index, and right of index, then take half from each.

        output = [arr[index]]

        left = max(0, index-k-1)
        right = min(len(arr)-1, index+k-1)

        while right-left+1>k:

            if left<0 or (x-arr[left])<=(arr[right]-x):
                right-=1
            elif right>len(arr)-1 or (x-arr[left])>(arr[right]-x):
                left+=1

        return arr[left:right+1]

    def findInsertionIndex(self, arr, x):
        low = 0
        high = len(arr)-1

        while low<high:
            mid = (low+high)//2

            if arr[mid]==x:
                return mid

            elif arr[mid]<x:
                low = mid+1
            else:
                high = mid

        return high
