class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        low = 0
        high = len(arr) - 1
        ans = ""

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return ans