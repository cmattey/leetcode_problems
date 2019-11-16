# Time: O(n)
# Space: O(n) , min(n,k) since only storing num%k element in map.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Lots of edge cases to take care of with 0.

        if a%k == b%k, then b-a%k==0
        eg: if a%k==3, b%k==3, then (a+3)%k==0, (b+3)%k==0, -> (b+3-(a+3))%k==0 -> b-a%k==0
        """

        imap = {}
        run_sum = 0

        imap[0] = -1
        for index, num in enumerate(nums):
            run_sum +=num
            if k!=0:
                run_sum = run_sum%k

            if run_sum in imap:
                if index-imap[run_sum]>1:
                    return True
            else: # notice the else condition, allows run_sum imap to grow larger, even if already exists, by not updating
                imap[run_sum]=index

        return False
