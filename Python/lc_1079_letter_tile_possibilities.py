# Time: O(n!)
# Space: O(n!)

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        seen = set()
        self.dfs([""], tiles, seen)

        print(seen)
        return len(seen)

    def dfs(self, cur_path, rest, seen):

        cur_word = "".join(cur_path)
        if cur_word not in seen and cur_word:
            seen.add(cur_word)

        for i, ch in enumerate(rest):
            cur_path.append(ch)
            self.dfs(cur_path, rest[:i]+rest[i+1:], seen)
            cur_path.pop()
