class Solution:

    def is_overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def merge_intervals(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if(len(intervals) < 1):
            return []

        res = []
        curr_interval = intervals[0]
        idx = 1

        while idx < len(intervals):
            if self.is_overlap(curr_interval, intervals[idx]):
                curr_interval = self.merge_intervals(
                    curr_interval, intervals[idx])
            else:
                res.append(curr_interval)
                curr_interval = intervals[idx]
            idx += 1
        res.append(curr_interval)

        return res
