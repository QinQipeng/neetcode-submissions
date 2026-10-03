class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if not newHead.next:
            self.tail = newHead
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(i < index and cur):
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail: # edge case if self.tail is to be removed
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        result = []
        cur = self.head.next
        while(cur):
            result.append(cur.val)
            cur = cur.next
        return result