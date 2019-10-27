# Time: O((m)*nlogn + mlogm + q*(plogp + log(m) )   n = avg_len(word), m = len(word), p = avg_len(query), q = len(query)
# Space: O(n + m + q + p)                       # calculation assuming, under the hood counter, and sorting

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        import bisect

        min_count = []
        for word in words:
            # word = "".join(sorted(word))          # Commented portion is verbose way, using counter
            min_ch = min(word)
            # min_ch = word[0]
            # c = collections.Counter(word)
            # min_ch_value = c[min_ch]
            min_ch_value = word.count(min_ch)
            min_count.append(min_ch_value)

        min_count.sort()

        output = []
        for query in queries:
            # query = "".join(sorted(query))
            # min_ch = query[0]
            min_ch = min(query)
            # c = collections.Counter(query)
            # min_ch_value = c[min_ch]
            min_ch_value = query.count(min_ch)
            count = 0
            index = bisect.bisect_right(min_count, min_ch_value)
            if index==len(min_count):
                count = 0
            else:
                count = len(min_count)-index

            output.append(count)

        return output
