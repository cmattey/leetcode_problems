# Time: O(n)
# Space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+','-','*','/']
        for el in tokens:
            if el in operators:
                second = stack.pop()
                first = stack.pop()

                if el=='+':
                    result = first+second
                elif el=='-':
                    result = first-second
                elif el=='*':
                    result = first*second
                elif el=='/':
                    result = int(first/second)
                stack.append(result)
            else:
                stack.append(int(el))


        return stack.pop()
                    
