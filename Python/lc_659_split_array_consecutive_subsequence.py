# Time: O(n)
# Space: O(n)

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import defaultdict
        num_map = defaultdict(int)
        end_map = defaultdict(int)

        for num in nums:
            if not num_map:
                num_map[num+1]+=1
                num_map[num+2]+=1
                end_map[num+2]+=1
            elif num_map[num]>0:
                num_map[num]-=1
            elif end_map[num-1]>0:
                end_map[num-1]-=1
                end_map[num]+=1
            else:
                num_map[num+1]+=1
                num_map[num+2]+=1
                end_map[num+2]+=1

        return not any(num_map.values())
            
