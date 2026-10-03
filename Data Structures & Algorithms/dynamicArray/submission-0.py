class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._storage = []
        self._tail = 0

    def get(self, i: int) -> int:
        return self._storage[i]

    def set(self, i: int, n: int) -> None:
        self._storage[i] = n

    def pushback(self, n: int) -> None:
        if (self._tail == self._capacity):
            self.resize()
        self._storage.append(n)
        self._tail += 1


    def popback(self) -> int:
        pop = self._storage.pop()
        self._tail -= 1
        return pop

    def resize(self) -> None:
        self._capacity *= 2


    def getSize(self) -> int:
        return self._tail
        
    
    def getCapacity(self) -> int:
        return self._capacity
