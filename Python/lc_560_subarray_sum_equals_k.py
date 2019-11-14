# Time: O(n)
# Space: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        sum = 0

        imap = collections.defaultdict(int)
        imap[0] = 1
        for num in nums:
            sum+=num
            count+=imap[sum-k]

            imap[sum]+=1

        return count


        """
        [1,1,1], k =2
             ^
        [1, 1, -1, -1, 2]

        Brute force: generate all subarrays O(n^3)

        count = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):

                cur_sum = sum(nums[left:right+1])
                if cur_sum==k:
                    count+=1

        return count

        repeated sums ^
        """


        """
        cumulative sums

        [1,1,1] -> [1,2,3] O(n^2) to find subarray sums compare every index to every next index

        [1,2,3] -> [0,1,3,6]

        count = 0

        cum_sum = [0]
        for num in nums:
            cum_sum.append(num+cum_sum[-1])

        for left in range(len(cum_sum)):
            for right in range(left+1, len(cum_sum)):
                # print(left, right)
                if cum_sum[right]-cum_sum[left]==k:
                    count+=1

        return count
        """



        
