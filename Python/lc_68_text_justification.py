class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        op = []

        wi = 0

        while wi<len(words):

            cur_line = ""

            while wi<len(words) and len(cur_line)<maxWidth:

                if len(cur_line)+len(words[wi]) == maxWidth:
                    cur_line += words[wi]
                    wi+=1
                    break
                elif len(cur_line)+len(words[wi]) > maxWidth:
                    break

                cur_line += words[wi]
                cur_line += " "
                wi+=1

            last_line = cur_line
            temp_words = cur_line.split(" ")

            # remove "" strings from split array
            cur_words = []
            for word in temp_words:
                if word:
                    cur_words.append(word)

            # justify using buckets
            num_buckets = 1 if len(cur_words)==1 else len(cur_words)-1

            total_spaces = maxWidth - sum(len(w) for w in cur_words)

            space_arr = [total_spaces//num_buckets]*num_buckets
            rem_space = total_spaces%num_buckets

            i = 0
            while rem_space>0:
                space_arr[i%len(space_arr)]+=1
                rem_space-=1
                i+=1

            new_line = []
            for w in cur_words:
                new_line.append(w)
                if space_arr:
                    new_line.append(" "*space_arr.pop(0))

            op.append("".join(new_line))

        # Left justify last line
        op.pop()

        rem_spaces = maxWidth - len(last_line)

        last_line+=" "*rem_spaces
        op.append(last_line)

        return op
