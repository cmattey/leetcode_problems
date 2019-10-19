# Time: O(n)
# Space: O(1)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        chunks = 0
        max_val = 0
        for index, val in enumerate(arr):

            max_val = max(max_val,val)

            if max_val == index:
                chunks+=1

        return chunks


# Time: O(n)
# Space: O(n)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # [2,0,1,4,3]

        found = [False]*len(arr)
        chunks = 0
        prev_start = 0
        for index, num in enumerate(arr):
            found[num] = True
            if not found[index]:
                found[num] = True
            elif found[index]:
                found[num] = True
                if all(val for val in found[prev_start:index]):
                    chunks+=1
                    prev_start = index+1

        return chunks
