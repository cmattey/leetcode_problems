# Time: O(n)
# Space: O(1)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        i_s, i_t = len(S)-1, len(T)-1
        count_s, count_t = 0, 0

        while i_s>=0 or i_t>=0:

            while i_s>=0:
                if S[i_s]=='#':
                    count_s+=1
                    i_s-=1
                elif count_s:
                    count_s-=1
                    i_s-=1
                else:
                    s_ch = S[i_s]
                    break

            while i_t>=0:

                if T[i_t]=='#':
                    count_t+=1
                    i_t-=1
                elif count_t:
                    count_t-=1
                    i_t-=1
                else:
                    t_ch = T[i_t]
                    break

            if i_s>=0 and i_t>=0:
                if S[i_s]!=T[i_t]:
                    return False

            if (i_s>=0) !=  (i_t>=0):
                return False

            i_s-=1
            i_t-=1

        return True

# Time: O(n)
# Space: O(n)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        return self.simplify(S)==self.simplify(T)

    def simplify(self, s):

        op = []
        for ch in s:
            if ch!='#':
                op.append(ch)
            else:
                if op:
                    op.pop()
        return "".join(op)
