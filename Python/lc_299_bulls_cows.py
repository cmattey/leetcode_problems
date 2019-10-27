# Time: O(m+n)
# Space: O(m+n)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:


        s_count = collections.Counter(secret)
        g_count = collections.Counter(guess)

#         First pass for bulls and reduce counts, doing separately cause, cows may consume all counts if counted first

        bulls = 0
        cows = 0

        for index, ch in enumerate(secret):
            if ch==guess[index]:
                s_count[ch]-=1
                g_count[ch]-=1
                bulls+=1

        # for index, ch in enumerate(secret):

        for key, value in s_count.items():

            if key in g_count and g_count[key]>0:
                cows+=min(s_count[key], g_count[key])
                # s_count[key]-=1
                # g_count[key]-=1

        op = []
        op.append(str(bulls))
        op.append("A")
        op.append(str(cows))
        op.append("B")

        return "".join(op)

        
