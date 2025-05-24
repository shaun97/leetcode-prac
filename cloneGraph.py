"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dictionary to store all of the new nodes
        # bfs to iterate through
        # we create the new node if the child of the curr node has an edge and it is not in the dict
        q = deque()

        newNodes = {}
        visited = set()

        if node == None:
            return None
        q.append(node)

        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)

            if curr.val not in newNodes:
                newNodes[curr.val] = Node()

            newNodes[curr.val].val = curr.val

            for neighbor in curr.neighbors:
                if neighbor.val not in newNodes:
                    newNodes[neighbor.val] = Node()
                newNodes[curr.val].neighbors.append(newNodes[neighbor.val])

                q.append(neighbor)

        return newNodes[1]


    def cloneGraphClean(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]