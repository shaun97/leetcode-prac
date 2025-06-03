
from collections import deque
class Solution:
   def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
    tracker1 = set()
    tracker2 = set()
    node1_curr = node1
    node2_curr = node2
    
    while node1_curr != -1 or node2_curr != -1:
        # Check if both paths reached the same node this iteration
        if node1_curr != -1 and node2_curr != -1 and node1_curr == node2_curr:
            return node1_curr
            
        # Check if current nodes were visited by the other path
        candidates = []
        
        if node1_curr != -1 and node1_curr in tracker2:
            candidates.append(node1_curr)
        if node2_curr != -1 and node2_curr in tracker1:
            candidates.append(node2_curr)
            
        if candidates:
            return min(candidates)
        
        # Add current nodes to trackers and advance
        if node1_curr != -1 and node1_curr not in tracker1:
            tracker1.add(node1_curr)
            node1_curr = edges[node1_curr]
        else:
            node1_curr = -1
            
        if node2_curr != -1 and node2_curr not in tracker2:
            tracker2.add(node2_curr)
            node2_curr = edges[node2_curr]
        else:
            node2_curr = -1
    
    return -1