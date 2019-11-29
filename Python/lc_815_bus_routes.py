# Nov 28th '19
# Time: O(sum(N*bi)), where N= num_busese = len(routes), bi = stops on bus_i
# Space: O(N(^2?) + sum(b_i)), N^2, cause in BFS, we can go from every stop to every other stop?

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        Need to take least number of buses from source to target.

        Each bus is represented as a node in the graph.
        From this node, adjacent nodes are all buses with a common stop with
        current bus_route.
        """

        bus_map = collections.defaultdict(set)

        for index, route in enumerate(routes):
            for stop in route:
                bus_map[index].add(stop)


        stop_map = collections.defaultdict(list)  # map to store stop->bus

        for bus_num, route in enumerate(routes):
            for stop in route:
                stop_map[stop].append(bus_num)

        seen_buses = set()
        q = [(S, 0)]

        while q:
            cur_stop, bus_count = q.pop(0)

            if cur_stop==T:
                return bus_count
#             for cur_stop, find all buses from it

            for bus in stop_map[cur_stop]:
                if bus not in seen_buses:
                    for stop in bus_map[bus]:
                        q.append((stop, bus_count+1))
                    seen_buses.add(bus)

        return -1

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
