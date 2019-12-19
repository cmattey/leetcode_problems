# Time: O(n), n = len(asteroids)
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            if not stack:
                stack.append(a)
            else:
                if stack[-1]>0 and a<0:
                    # collision
                    nxt = a
                    while stack and stack[-1]>0 and nxt<0:

                        top = stack.pop()

                        if abs(top)>abs(nxt):
                            stack.append(top)
                            nxt = top
                        elif abs(top)<abs(nxt):
                            # stack.append(nxt)
                            nxt = a
                            continue
                        else: # top==nxt
                            nxt = 0
                            break

                    if nxt<0:
                        stack.append(nxt)

                else: # if nxt a is positive, or if nxt a is
                    stack.append(a)

        return stack
