# Review Mar 9th '20'
# Time: O(N)
# Space: O(N)
class Solution:
    def uniqueLetterString(self, s: str) -> int:

        import collections

        ch_map = collections.defaultdict(list)

        for index, ch in enumerate(s):
            ch_map[ch].append(index)

        total_count = 0

        for ch, pos in ch_map.items():
            pos = [-1]+pos+[len(s)]

            for i in range(1,len(pos)-1):
                total_count += (pos[i]-pos[i-1])*(pos[i+1]-pos[i])

        return total_count%(10**9 + 7)

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
