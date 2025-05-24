from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a max heap p queue of size k
        # loop through every point and add it to the pqueue

        q = PriorityQueue()

        for point in points:
            dist = -1 * math.sqrt(point[0] ** 2 + point[1] ** 2)
            q.put((dist, point))
            if q.qsize() > k:
                q.get()

        res = []
        while q.qsize() > 0:
            point = q.get()
            res.append(point[1])

        return res
