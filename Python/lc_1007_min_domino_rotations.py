# Nov 17th '19
# Time: O(n)
# Space: O(1)
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        min_a = self.min_count(A[0], A, B)
        return min_a if min_a!=-1 else self.min_count(B[0], A, B)

    def min_count(self, el, A, B):
        """
        Number of ways to convert all elements of A and B into el
        """
        swaps_a = 0
        swaps_b = 0
        for i in range(len(A)):
            if A[i]!=el and B[i]!=el:
                return -1
            elif A[i]!=el: # and B[i]==el
                swaps_a+=1
            elif B[i]!=el: # and A[i]==el
                swaps_b+=1

        return min(swaps_a, swaps_b)

# Time: O(min(a,b))
# Space: O(a+b)

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        first two tiles are key,
        Three cases follows:
        - Nothing matches, return -1
        - exactly one of the rows match, proceed linearly with the matched element.
        - Both match, need to proceed with both tiles.
        """

        count_a = collections.Counter(A)
        count_b = collections.Counter(B)
        max_el_a, max_count_a = count_a.most_common(1)[0]
        max_el_b, max_count_b = count_b.most_common(1)[0]
        # max_count_a = count_a[max_el_a]
        # max_count_b = count_b[max_el_b]

        target_arr = 'a'
        if max_count_a>max_count_b:
            max_el = max_el_a
            target_arr = 'a'
        else:
            max_el = max_el_b
            target_arr = 'b'

        # print(max_el, target_arr)
        num_swaps = 0
        if target_arr == 'a':

            for index, ch in enumerate(A):
                if ch!=max_el and B[index]==max_el:
                    num_swaps+=1
                elif ch==max_el:
                    continue
                else:
                    return -1

        else:
            for index, ch in enumerate(B):
                if ch!=max_el and A[index]==max_el:
                    num_swaps+=1
                elif ch==max_el:
                    continue
                else:
                    return -1

        return num_swaps
