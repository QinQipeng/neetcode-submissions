class TimeMap:

    def __init__(self):
        self.store: dict[str, [(int, str)]] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
         self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyList = self.store.get(key, [])
        if len(keyList) == 0:
            return ""

        L, R = 0, len(keyList) - 1
        res = ""

        while L <= R:
            mid = (L + R) // 2
            if keyList[mid][0] < timestamp:
                L = mid + 1
                res = keyList[mid][1]
            elif timestamp < keyList[mid][0]:
                R = mid - 1
            else:
                return keyList[mid][1]
        return res
