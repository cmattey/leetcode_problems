# 763. Partition Labels
# Time: O(len(S))
# Space:O(len(S))
class Solution:
    def partitionLabels(self, S: str) -> List[int]:


        start = 0
        end = len(S)-1

        cur_start = 0
        cur_end = -1

        range_map = {}

        for index,ch in enumerate(S):
            range_map[ch] = index


        range_list = []
        while start<len(S):
            cur_start = start
            cur_end = range_map[S[start]]

            while cur_start<cur_end and cur_start+1<len(S):
                cur_start+=1
                temp_end = range_map[S[cur_start]]

                cur_end = max(cur_end, temp_end)

            range_list.append(cur_end-start+1)

            start = cur_start+1

        return range_list
