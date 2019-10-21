# Time: O(nlogn)
# Space: O(n)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        arr_s = sorted(arr)

        loc_map_s = collections.defaultdict(list)

        for index, el in enumerate(arr_s):

            loc_map_s[el].append(index)

        chunks = 0
        max_index = -1

        for index, el in enumerate(arr):

            max_index = max(loc_map_s[el].pop(0), index, max_index)

            if index==max_index:
                chunks+=1

        return chunks
