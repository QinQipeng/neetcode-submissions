class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        while(curr):
            if (index == 0):
                return curr.val
            curr = curr.next
            index -= 1
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
        curr = self.head
        while(i < index and curr):
            curr = curr.next
            i += 1
        if (curr and curr.next):
            if (curr.next == self.tail):
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while( curr ):
            result.append(curr.val)
            curr = curr.next
        return result


        
