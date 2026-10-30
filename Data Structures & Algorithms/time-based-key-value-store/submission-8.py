class TimeMap:

    def __init__(self):
        self.table: dict[str, [tuple[int, str]]] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyList = self.table[key]
        left, right = 0, len(keyList) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if keyList[mid][0] <= timestamp:
                result = keyList[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
