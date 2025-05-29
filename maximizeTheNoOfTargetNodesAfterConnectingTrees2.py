from collections import deque, defaultdict

class Solution:
    def count_nodes_by_parity(self, start, adjList):
        """Count nodes at levels with specified parity (0 for even, 1 for odd)"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        level = 0
        color = 0

        res = {} #colour of the node
        
        while queue:
            level_size = len(queue)
            
            # Count nodes at current level if parity matches
            color = (color+3) % 2
        
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                res[node] = color
                for neighbor in adjList[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            level += 1
        
        return res
    
    def build_adjacency_list(self, edges):
        """Build bidirectional adjacency list"""
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj
    
    def maxTargetNodes(self, edges1, edges2):
        # Build adjacency lists
        adj1 = self.build_adjacency_list(edges1)
        adj2 = self.build_adjacency_list(edges2)

        maxColor = 1
        if len(edges2) > 1:
            color2 = self.count_nodes_by_parity(0, adj2)
            noOfColor1, noOfColor2 = 0, 0
            for k, v in color2.items():
                if v == 0:
                    noOfColor1 += 1
                else:
                    noOfColor2 += 1
            maxColor = max(noOfColor1, noOfColor2)
        
        color1 = self.count_nodes_by_parity(0, adj1)
        res = [0 for _ in range(len(adj1))]
        color11, color12 = 0, 0
        for k, v in color1.items():
            if v == 0:
                color11 += 1
            else:
                color12 += 1
        for k, v in color1.items():
            if v == 0:
                res[k] = color11 + maxColor
            else:
                res[k] = color12 + maxColor
        
        return res