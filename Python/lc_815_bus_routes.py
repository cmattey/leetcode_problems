# Time: O(N(^2?)+num_stops), where N=len(routes) <--Review
# Space: O(N+num_stops), where N=len(routes)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        Requirement is to find min number of buses, therefore, graph with stops as nodes
        isn't the best approach.

        Maintain two graphs:
        bus_map: Key:bus_num(using index in routes),values:[bus_stops]
        buses_at_stop_map: Key:bus_stop, value: buses that arrive at that stop.

        Do bfs starting from each bus, that arrives at stop S.

        """
        from collections import defaultdict

        bus_map = defaultdict(set)
        buses_at_stop_map = defaultdict(set)

        for bus_num, route in enumerate(routes):
            for stop in route:
                bus_map[bus_num].add(stop)
                buses_at_stop_map[stop].add(bus_num)

        seen_stops = set()
        q = [(S,0)]
        seen_buses = set()
        while q:
            cur_stop, num_buses = q.pop(0)

            if cur_stop==T:
                return num_buses
            if cur_stop in seen_stops:
                continue
            seen_stops.add(cur_stop)

            for bus in buses_at_stop_map[cur_stop]:
                if bus in seen_buses:
                    continue
                seen_buses.add(bus)
                for stop in bus_map[bus]:
                    if stop not in seen_stops:
                        q.append((stop,num_buses+1))

        return -1
