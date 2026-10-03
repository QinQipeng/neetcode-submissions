class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def insert(self, key: int, value: int) -> None:
        new_pair = Pair(key, value)
        index = key % self.capacity
        for pair in self.table[index]:
            if pair.key == key:
                pair.value = value
                return
        
        self.table[index].append(new_pair)
        self.size += 1

        if (self.size / self.capacity >= 0.5):
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        for pair in self.table[index]:
            if pair.key == key:
                self.table[index].remove(pair)
                self.size -= 1
                return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        oldHash = []
        for buckets in self.table:
            oldHash.extend(buckets)
        
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        for pair in oldHash:
            index = pair.key % self.capacity
            self.table[index].append(pair)

