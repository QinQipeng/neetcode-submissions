class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.insert(0, value)

    def pop(self) -> int:
        return -1 if self.isEmpty() else self.queue.pop()

    def popleft(self) -> int:
        return -1 if self.isEmpty() else self.queue.pop(0)
