# 71. Simplify Path
# Time: O(len(path))
# Space: O(len(path))
class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = path.split('/')
        stack = []
        for dir in dirs:
            if dir not in ['.', '..','']:
                stack.append(dir)
            elif dir =='..' and stack:
                stack.pop()

        return "/"+"/".join(stack)
