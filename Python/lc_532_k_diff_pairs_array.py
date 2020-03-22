# Time: O(n)
# Space: O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        import collections

        count_map = collections.defaultdict(int)

        for num in nums:
            count_map[num]+=1

        ans = 0
        for num in count_map:

            if k>0 and num+k in count_map:
                ans+=1
            elif k==0 and count_map[num]>1:
                ans+=1

        return ans

# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen_pairs = set()

        nums.sort()

        print(nums)
        start = 0
        end = 1

        ans = 0
        while start<end and end<len(nums):

            if nums[end]-nums[start]>k:
                start+=1
                if start==end:
                    end+=1
            elif nums[end]-nums[start]<k:
                end+=1
            else:
                cur_pair = (nums[start], nums[end])
                if cur_pair not in seen_pairs:
                    seen_pairs.add(cur_pair)
                    ans+=1

                start+=1
                end+=1

        return ans
