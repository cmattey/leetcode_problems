# Oct 29th '19
# Time: O(n)
# Space: O(unique(n))
class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        count_map = collections.defaultdict(int)
        end_map = collections.defaultdict(int)

        for num in nums:

            if count_map[num]==0 and end_map[num-1]==0:
                count_map[num+1]+=1
                count_map[num+2]+=1
                end_map[num+2]+=1
            elif count_map[num]>0:
                count_map[num]-=1
            elif end_map[num-1]>0:
                end_map[num-1]-=1
                end_map[num]+=1
            else:
                return False

        return not any(val for val in count_map.values())

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
