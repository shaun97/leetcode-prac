class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Traverse the intervals and find the point that it should be inserted in, start i > start i - 1.
        # Check the previous interval and all subsequent intervals to see if they should be merged.

        if intervals == []:
            return [newInterval]

        insertion_idx = -1
        for idx, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                insertion_idx = idx
                intervals.insert(insertion_idx, newInterval)
                break
            elif idx == (len(intervals) - 1):
                insertion_idx = idx + 1
                intervals.insert(insertion_idx, newInterval)
                break

        print(intervals)
        check_idx = max(0, insertion_idx - 1)

        while check_idx < (len(intervals) - 1):
            if intervals[check_idx][1] >= intervals[check_idx + 1][0]:
                intervals[check_idx][1] = max(
                    intervals[check_idx + 1][1], intervals[check_idx][1])
                del intervals[check_idx + 1]
            else:
                check_idx += 1

        return intervals
