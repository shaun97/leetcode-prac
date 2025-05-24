class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFSfrom pacific and note down all nodes that can be reached
        # BFS from atlantic and note down all nodes that can reach the atlantic
        res = []
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        pacificq = deque()
        pacificVisited = set()

        m = len(heights)
        n = len(heights[0])

        # Fill up the pacfic queue with top row
        for i in range(m):
            pacificq.append((i, 0))

        # Fill up pacific queue with bottom row
        for i in range(n):
            pacificq.append((0, i))

        # BFS on the pacfic q
        while pacificq:
            currX, currY = pacificq.popleft()
            currHeight = heights[currX][currY]

            if (currX, currY) in pacificVisited:
                continue
            else:
                pacificVisited.add((currX, currY))

            for x, y in directions:
                newX, newY = currX + x, currY + y

                if newX > -1 and newY > -1 and newX < m and newY < n:
                    newHeight = heights[newX][newY]
                    if currHeight <= newHeight:
                        pacificq.append((newX, newY))

        atlanticq = deque()
        atlanticVisited = set()

        for i in range(m):
            atlanticq.append((i, n - 1))
        for i in range(n):
            atlanticq.append((m - 1, i))

        while atlanticq:
            currX, currY = atlanticq.popleft()
            currHeight = heights[currX][currY]

            if (currX, currY) in atlanticVisited:
                continue
            else:
                atlanticVisited.add((currX, currY))

            if (currX, currY) in pacificVisited:
                res.append([currX, currY])

            for x, y in directions:
                newX, newY = currX + x, currY + y

                if newX > -1 and newY > -1 and newX < m and newY < n:
                    newHeight = heights[newX][newY]
                    if currHeight <= newHeight:
                        atlanticq.append((newX, newY))

        return res
