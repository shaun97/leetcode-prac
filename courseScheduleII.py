class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topo sort of all the courses
        # Create an adj list and an indegree dictionary
        # apply dfs -> every time you encounter a node that comes before another, decrement the indegree of the second node
        # if indegree is 0, then add it to the queue
        # store the list of nodes that you visited
        adjList = {}
        inDegrees = {}
        res = []
        for prerequisite in prerequisites:
            second, first = prerequisite
            if first not in adjList:
                adjList[first] = []
            adjList[first].append(second)
            if second not in inDegrees:
                inDegrees[second] = 0
            inDegrees[second] += 1

        for i in range(numCourses):
            if i not in inDegrees:
                inDegrees[i] = 0

        q = deque()
        for key, item in inDegrees.items():
            if item == 0:
                q.append(key)
        # DFS
        while q:
            node = q.pop()
            del inDegrees[node]
            res.append(node)
            if node not in adjList:
                continue

            for neighbour in adjList[node]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    q.append(neighbour)
        print(inDegrees)
        if len(inDegrees) > 0:
            return []
        else:
            return res
