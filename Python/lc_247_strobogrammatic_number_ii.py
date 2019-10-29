# Time: 5^(n), each call to n is wrapped by 5 chars(max) <- check
# Space: 5^n

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        if n==1:
            return ["0","1","8"]

        if n==2:
            return ["11","69","88","96"]

        return self.rec(n)


    def rec(self, n):
        if n==1:
            return ["0","1","8"]
        elif n==2:
            return ["00","11","69","88","96"]

#         3 = ["101","111","181","609","619","689","808","818","888","906","916","986"]
#         4 = ["1111","8888","6969","9696",...]

        if n%2==0:
            if n==4:
                prev_seq = self.rec(n-2)[1:]
            else:
                prev_seq = self.rec(n-2)

            new_seq = []
            orig = self.rec(2)

            mid = (n-2)//2
            for prev in prev_seq:
                for og in orig:
                    new_seq.append(prev[:mid]+og+prev[mid:])

            return new_seq

        else:
            if n==3:
                prev_seq = self.rec(n-1)[1:]
            else:
                prev_seq = self.rec(n-1)

            new_seq = []
            orig = self.rec(1)
            mid = (n-1)//2
            for prev in prev_seq:
                for og in orig:
                    new_seq.append(prev[:mid]+og+prev[mid:])

            return new_seq
    
