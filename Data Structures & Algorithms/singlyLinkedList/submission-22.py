class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if index == i:
                return cur.value
            cur = cur.next    
            i+=1
            
        return -1
            

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if (not newNode.next):
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(i < index and cur):
            cur = cur.next
            i += 1
        if (cur and cur.next):
            if(cur.next == self.tail):
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        result = []
        cur = self.head.next
        while (cur):
            result.append(cur.value)
            cur = cur.next
        return result

        
