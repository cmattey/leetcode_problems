# Time: O(num_words*avg_len(word)) O(V+E) <- Topological Sort check
# Space:O(num_words*avg_len(word)) O(V+E)

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Make graph of dependencies(orders).
        Note: We are given words which themselves aren't sorted, but the words are given in dictionary order.
        """

        dep_map = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        seen_chars = set(ch for word in words for ch in word)

        for index in range(len(words)-1):
            cur_word = words[index]
            next_word = words[index+1]

            for i, ch in enumerate(cur_word):
                if i<len(next_word) and ch!=next_word[i]:
                    dep_map[ch].append(next_word[i])
                    in_degree[next_word[i]]+=1
                    break

        indies = [val for val in seen_chars if val not in in_degree]

        order = []

        while indies:

            cur_ch = indies.pop(0)
            order.append(cur_ch)
            for dep_char in dep_map[cur_ch]:
                in_degree[dep_char]-=1

                if in_degree[dep_char]==0:
                    indies.append(dep_char)


        return "".join(order) if len(order)==len(seen_chars) else ""
