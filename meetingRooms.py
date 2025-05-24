class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort via starting time
        # iterate through the all the intervals, if any end > start, return false

        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
