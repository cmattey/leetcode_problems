class Solution:
    def checkValidString(self, s: str) -> bool:

        count = 0
        count_star = 0
        for ch in s:

            if ch=="(":
                count+=1
            elif ch=="*":
                count_star+=1
            else:
                count-=1
                if count<0:
                    if count_star>0:
                        count_star-=1
                        count+=1
                    else:
                        return False
        count = 0
        count_star = 0
        for ch in reversed(s):
            if ch==")":
                count+=1
            elif ch=="*":
                count_star+=1
            else:
                count-=1
                if count<0:
                    if count_star>0:
                        count_star-=1
                        count+=1
                    else:
                        return False

        return True
        
