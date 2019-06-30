# 1106. Parsing A Boolean Expression
# Weekly Contest 143
# To be Refactored
# Time: O(len(expression))
# Space: O(len(expression))
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch in ['&','|','!']:
                stack.append(ch)
            elif ch == ')':
                ch = stack.pop()
                arr = []
                while ch not in ['&','|','!'] and stack:
                    arr.append(ch)
                    ch = stack.pop()

                if ch == '&':
                    result = True
                    for tf in arr:
                        result = result and tf

                    stack.append(result)

                elif ch == '|':
                    result = False
                    for tf in arr:
                        result = result or tf

                    stack.append(result)
                elif ch == '!':
                    result = not arr[0]

                    stack.append(result)

            elif ch in [',','(',]:
                continue
            elif ch =='t':
                stack.append(True)
            elif ch == 'f':
                stack.append(False)


        ans = stack.pop()
        return ans
