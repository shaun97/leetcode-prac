class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # least number of buses 
        # buses and edges alternate as nodes
        # takes in bus -> routes
        # stop
        # takes in stop -> bus
        stopAdjList = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopAdjList:
                    stopAdjList[stop] = []
                stopAdjList[stop].append(bus)

        q = deque()
        visited = set()
        # we alternate dfs between bus and stop, if node is bus, we add the stops it visits
        # bfs
        BUS = "BUS"
        STOP = "STOP"
        DELIM = "DELIM"
        q.append((STOP, source))
        isBus = False
        noOfBuses = 0

        while q:
            nodeType, val = q.popleft()
            if (nodeType, val) in visited:
                continue
            visited.add((nodeType, val))

            if nodeType == STOP:
                isBus = False
                if val == target:
                    return noOfBuses
                buses = stopAdjList[val]
                for bus in buses:
                    q.append((BUS, bus))
            else:
                if not isBus:
                    noOfBuses += 1
                isBus = True
                stops = routes[val]
                for stop in stops:
                    q.append((STOP, stop))
        
        return -1