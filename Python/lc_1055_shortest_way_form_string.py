# Nov 15th '19
# Time: O(src*target)
# Space: O(1)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        if len(set(source)&set(target)) < len(set(target)):
            return -1

        start_index = 0
        count = 1
        for ch in target:

            start_index = source.find(ch, start_index)

            if start_index==-1:
                start_index = source.find(ch)
                count+=1

            start_index+=1

        return count

# Nov 11th '19
# Time: O(src*target)
# Space: O(1)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        min_count = 1

        if len(set(source)&set(target)) < len(set(target)):
            return -1

        cur_loc = 0
        t_index = 0
        while t_index<len(target):

            find_index = source.find(target[t_index], cur_loc)

            if find_index!=-1:
                cur_loc = find_index+1
                t_index+=1
            elif find_index==-1:
                cur_loc = 0
                min_count+=1

        return min_count


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
