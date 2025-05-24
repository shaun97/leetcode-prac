class TimeMap:

    def __init__(self):
        # dictionary of a sorted list -> since the timestamp of set is strictly increasing, we dont have to sort this
        # should be a tuple in the sorted list
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add to the dict and the list
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search -> first value that is smaller than the timestamp
        if key not in self.timeMap:
            return ""

        listOfTimeStamps = self.timeMap[key]
        # for i in range(len(listOfTimeStamps) - 1, -1, -1):
        #     if listOfTimeStamps[i][0] <= timestamp:
        #         return listOfTimeStamps[i][1]

        # Binary search
        left = 0
        right = len(listOfTimeStamps) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == right:
                if listOfTimeStamps[mid][0] == timestamp:
                    return listOfTimeStamps[mid][1]
                else:
                    break
            elif listOfTimeStamps[mid][0] <= timestamp and listOfTimeStamps[mid + 1][0] > timestamp:
                return listOfTimeStamps[mid][1]
            elif listOfTimeStamps[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
                # 1 2 3 5 6 10 -> 4

        mid = left + (right - left) // 2
        if listOfTimeStamps[mid][0] < timestamp:
            return listOfTimeStamps[mid][1]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
