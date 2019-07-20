# 78. Subsets
# Time: O(2^(len(nums))*len(nums))
# Space: O(2^(len(nums))*len(nums)) For creating string binary
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        iters = int(math.pow(2,len(nums)))

        subsets = []
        for i in range(iters):
            binary = bin(i)[2:]

            rem_zero = len(nums)-len(binary)
            binary = '0'*rem_zero + binary

            cur_set = []
            for index,ch in enumerate(binary):
                if ch=='1':
                    cur_set.append(nums[index])

            subsets.append(cur_set)

        return subsets
