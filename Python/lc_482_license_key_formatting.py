# Time: O(len(S))
# Space: O(len(S))

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.upper()

        S = S.split('-')
        S = "".join(S)
        rem = len(S)%K

        op = []
        if rem>0:
            op = list(S[:rem])

        rem_str = []
        for index, ch in enumerate(S[rem:]):
            if index%K==0:
                rem_str.append('-')

            rem_str.append(ch)


        op = op + rem_str
        lic = "".join(op)

        if len(lic)>0 and lic[0]=='-':
            lic = lic[1:]

        return lic
                    
