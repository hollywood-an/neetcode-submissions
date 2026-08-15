class TimeMap:

    def __init__(self):
        self.time = {}
        #key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        if timestamp > len(self.time[key]):
            return self.time[key][len(self.time[key])-1][0]
        #binary search
        left = 0
        right = len(self.time[key])-1
        while left <= right:
            mid = (left + right) // 2

            t = self.time[key][mid][1]
            if t == timestamp:
                return self.time[key][mid][0]
            if t > timestamp:
                right = mid - 1
            else:
                left = mid + 1

