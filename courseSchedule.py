class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Convert this into a graph and perform DFS to check if you can reach numCourses - 1 from 0
        adjList = {}
        for prereq in prerequisites:
            if prereq[1] not in adjList:
                adjList[prereq[1]] = []
            adjList[prereq[1]].append(prereq[0])

        visited = [False] * numCourses
        path = [False] * numCourses

        for course in range(numCourses):
            if self.isCyclic(path, visited, adjList, course):
                return False
        return True

    def isCyclic(self, path, visited, adjList, node):
        if visited[node]:
            return False

        if path[node]:
            return True

        if node not in adjList:
            return False

        path[node] = True

        ret = False

        for child in adjList[node]:
            ret = self.isCyclic(path, visited, adjList, child)
            if ret:
                break

        path[node] = False
        visited[node] = True
        return ret


# TOP SORT


class GNode(object):
    """  data structure represent a vertex in the graph."""

    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []


class SolutionTopSort(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False
