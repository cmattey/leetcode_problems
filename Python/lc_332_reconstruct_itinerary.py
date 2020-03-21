class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import collections

        route_map = collections.defaultdict(list)

        for ticket in tickets:
            route_map[ticket[0]].append(ticket[1])

        for source, dest_list in route_map.items():
            dest_list.sort(reverse=True)

        stack = ["JFK"]
        route = []

        while stack:

            while route_map[stack[-1]]:
                stack.append(route_map[stack[-1]].pop())

            route.append(stack.pop())

        return route[::-1]
