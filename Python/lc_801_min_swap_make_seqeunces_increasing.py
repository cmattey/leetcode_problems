# Time: O(n)
# Space: O(1)

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        [1,6,5]
        [3,4,7]
        make 2 arrays:
        swap[i] = num_swap to make prefix [i] sorted, by swapping the ith column
        no_swap[i] = num_swap to make prefix [i] sorted, without swapping the ith column
        """

        swap = 1
        no_swap = 0

        for i in range(1,len(A)):

            new_swap = float('inf')
            new_no_swap = float('inf')
            if A[i-1]<A[i] and B[i-1]<B[i]:
                new_swap = swap+1
                new_no_swap = no_swap

            if A[i-1]<B[i] and B[i-1]<A[i]:
                new_swap = min(new_swap, no_swap+1)
                new_no_swap = min(swap, new_no_swap)

            swap = new_swap
            no_swap = new_no_swap
        # print(swap, no_swap)
        return min(swap, no_swap)


# Time: O(n)
# Space: O(n)

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        [1,6,5]
        [3,4,7]
        make 2 arrays:
        swap[i] = num_swap to make prefix [i] sorted, by swapping the ith column
        no_swap[i] = num_swap to make prefix [i] sorted, without swapping the ith column
        """

        swap = [float('inf')]*len(A)
        no_swap = [float('inf')]*len(A)

        swap[0] = 1
        no_swap[0] = 0

        for i in range(1,len(A)):

            if A[i-1]<A[i] and B[i-1]<B[i]:
                swap[i] = swap[i-1]+1
                no_swap[i] = no_swap[i-1]

            if A[i-1]<B[i] and B[i-1]<A[i]:
                swap[i] = min(swap[i], no_swap[i-1]+1)
                no_swap[i] = min(swap[i-1], no_swap[i])

        print(swap, no_swap)
        return min(swap[-1], no_swap[-1])
