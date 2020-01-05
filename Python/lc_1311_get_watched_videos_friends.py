# LC Contest 170
# Time: O(V+E), V = vertices(len(friends)), E = edges(friend connections)
# Space: O(V+E), for storing graph

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        from collections import defaultdict

        g = {}

        for i in range(len(friends)):
            g[i] = friends[i]

        seen = set()
        q = [(id, 0)]

        targets = []
        while q:
            cur_person, cur_dep = q.pop(0)
            if cur_person in seen:
                continue

            seen.add(cur_person)
            if cur_dep==level:
                targets.append(cur_person)

            for nei in g[cur_person]:
                q.append((nei, cur_dep+1))

        op = defaultdict(int)
        for t in targets:
            for vid in watchedVideos[t]:
                op[vid]+=1

        return sorted(list(op.keys()), key = lambda k: (op[k], k))
