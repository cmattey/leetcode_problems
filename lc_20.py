# 20. Valid Parentheses
# Time: O(len(s))
# Space: O(len(s))
class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {')':'(',
              ']':'[',
              '}':'{'}

        stack = []
        for ch in s:
            if ch in bracket_map and not stack:
                return False
            elif ch in bracket_map:
                if stack.pop() != bracket_map[ch]:
                    return False
            else:
                stack.append(ch)

        if not stack:
            return True

        return False
