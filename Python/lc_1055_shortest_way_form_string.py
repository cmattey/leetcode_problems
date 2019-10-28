# Time: O(src*target), because of search
# Space: O(1), if not accounting for set creation at beginning.

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        if len(set(source)&set(target))<len(set(target)):
            return -1


        prev_index = 0
        min_seq_count = 1
        for ch in target:

            new_loc = source.find(ch, prev_index)

            if new_loc==-1:
                min_seq_count+=1
                prev_index = source.find(ch)+1

#               no need to do check for -1, since that's covered at the start
#               if prev_index==-1: return -1

            else:
                prev_index = new_loc+1

        return min_seq_count
