# Time: O(s+t)
# Space: O(max(s,t)), can be done in constant space using pointers
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        stack = []

        for ch in S:
            if ch!='#':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()

        word1 = "".join(stack)
        stack = []
        for ch in T:
            if ch!='#':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()

        word2 = "".join(stack)

        return word1==word2


# Time: O(len(S)+len(T))
# Space: O(len(S)+len(T))

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Can be done in constant space
        """
        stack1 = []
        stack2 = []

        i1,i2 = 0,0

        while i1<len(S) or i2<len(T):

            # print(i1,i2)
            # print(stack1, stack2)
            if i1<len(S) and S[i1]=='#':
                if stack1:
                    stack1.pop()
                i1+=1
            elif i2<len(T) and T[i2]=='#':
                if stack2:
                    stack2.pop()
                i2+=1
            elif i1<len(S):
                stack1.append(S[i1])
                i1+=1
            elif i2<len(T):
                stack2.append(T[i2])
                i2+=1

        return stack1==stack2
