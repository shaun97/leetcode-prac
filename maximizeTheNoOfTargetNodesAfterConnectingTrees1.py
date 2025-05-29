maximizeTheNoOfTargetNodesAfterConnectingTrees1.py
from collections import deque 
class Solution:
    def bfs(self, node, edges, k):
        if k < 0:
            return 0
        q = deque()
        q.append(node)
        q.append(-1)
        count = 0
        visited = set()
        level = 0
        while q:
            node = q.popleft()
            if node == -1:
                level += 1
                if level > k:
                    break
                q.append(-1)
                continue
            visited.add(node)
            count += 1
            for child in edges[node]:
                if child in visited:
                    continue
                q.append(child)
        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        edgeMap1 = {}
        edgeMap2 = {}
        for i in edges1:
            source, des = i
            if source not in edgeMap1:
                edgeMap1[source] = []
            if des not in edgeMap1:
                edgeMap1[des] = []
            edgeMap1[source].append(des)
            edgeMap1[des].append(source)
        for i in edges2:
            source, des = i
            if source not in edgeMap2:
                edgeMap2[source] = []
            if des not in edgeMap2:
                edgeMap2[des] = []
            edgeMap2[source].append(des)
            edgeMap2[des].append(source)
        maxCount = 0
        for key in edgeMap2:
            maxCount = max(maxCount, self.bfs(key, edgeMap2, k-1))
        res = [0 for _ in range(len(edgeMap1))]
        for i in range(len(res)):
            res[i] = self.bfs(i, edgeMap1, k) + maxCount
        return res
