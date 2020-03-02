# Time: O(N), max chars 52
# Space: O(N)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        import collections
        count_map = collections.defaultdict(list)

        for index, ch in enumerate(s):
            count_map[ch].append(index)


        total = 0
        for key , value in count_map.items():

            vals = [-1]+value+[len(s)]

            for i in range(1, len(vals)-1):

                total+= (vals[i]-vals[i-1])*(vals[i+1]-vals[i])

        return total %(10**9 + 7)
