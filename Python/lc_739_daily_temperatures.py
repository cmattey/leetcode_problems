# Time: O(n)
# Space: O(n)

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        stack = []

        output = [0]*len(T)

        for index, temp in enumerate(T):

            while stack and stack[-1][1]<temp:

                popped = stack.pop()
                output[popped[0]] = index-popped[0]

            stack.append([index,temp])

        return output
        
