class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}

        for edge in edges:
            node1, node2 = edge
            if adjList.get(node1):
                adjList[node1].append(node2)
            else:
                adjList[node1] = [node2]

            if adjList.get(node2):
                adjList[node2].append(node1)
            else:
                adjList[node2] = [node1]

        noOfConnectedComponents = 0
        visited = set()

        for node in range(n):
            if node in visited:
                continue
            else:
                noOfConnectedComponents += 1
                q = deque()
                q.append(node)

                while q:
                    currNode = q.popleft()
                    if currNode in visited:
                        continue
                    else:
                        visited.add(currNode)

                    if adjList.get(currNode):
                        for neighbour in adjList[currNode]:
                            q.append(neighbour)

        return noOfConnectedComponents
