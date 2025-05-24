from collections import deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # It must be that it has this number of edges
        if len(edges) != n - 1: return False

        # Another way of intialising the adj list
        # adj_list = [[] for _ in range(n)]
        # for A, B in edges:
        #     adj_list[A].append(B)
        #     adj_list[B].append(A)
        adjList = {}
        for node1, node2 in edges:
            if adjList.get(node1):
                adjList[node1].append(node2)
            else:
                adjList[node1] = [node2]

            if adjList.get(node2):
                adjList[node2].append(node1)
            else:
                adjList[node2] = [node1]

        q = deque()
        visited = set()
        if len(edges) > 0:
            q.append((edges[0][0], -1))

        while q:
            node, parent = q.pop()

            if node in visited:
                return False
            visited.add(node)
            for adjNode in adjList[node]:
                if adjNode == parent:
                    continue
                q.append((adjNode, node))

        if len(visited) < n:
            return False
        else:
            return True
