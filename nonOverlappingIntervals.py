class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy solution where we sort by the start point
        # sort the array by start
        # when we iterate through, if there is an overlap
        # remove the one that is within
        # remove the later one
        res = 0
        intervals.sort(key=lambda x: x[0])

        first = 0
        second = 1
        while second < len(intervals):
            firstInterval = intervals[first]
            secondInterval = intervals[second]

            # overlap
            if firstInterval[1] > secondInterval[0]:
                # remove second one
                if secondInterval[1] > firstInterval[1]:
                    second += 1
                    res += 1
                # remove the first one
                else:
                    # remove the first
                    first = second
                    second += 1
                    res += 1
            else:
                first = second
                second += 1
        return res
