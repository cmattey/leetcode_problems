class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()

        while n!=1:
            if n in seen_set:
                return False

            seen_set.add(n)
            n = self.sum_digits(n)
        return True

    def sum_digits(self, n):

        s = 0
        while n>0:
            last_digit = n%10
            s+=last_digit**2
            n=n//10

        return s
        
