class TreeNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def _recurInsert(node, key, val) -> TreeNode:
            if node == None:
                return TreeNode(key, val)
            if key == node.key:
                node.value = val
            elif key < node.key:
                node.left = _recurInsert(node.left, key, val)
            elif key > node.key:
                node.right = _recurInsert(node.right, key, val)
            return node

        self.root = _recurInsert(self.root, key, val)
        

    def get(self, key: int) -> int:
        def _recurGet(node, key):
            if node == None:
                return -1
            if key == node.key:
                return node.value
            return _recurGet(node.left, key) if key < node.key else _recurGet(node.right, key)

        return _recurGet(self.root, key)

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        
        return curr.value if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        
        return curr.value if curr else -1

    def remove(self, key: int) -> None:
        def findMin(node) -> int:
            curr = node
            while curr and curr.left:
                curr = curr.left
            
            return curr

        def _recurRemove(node, key):
            if node == None:
                return None
            if key == node.key:
                if not (node.left and node.right):
                    return node.right if node.right else node.left
                else:
                    minNode = findMin(node.right)
                    node.key = minNode.key
                    node.value = minNode.value
                    node.right = _recurRemove(node.right, minNode.key)

            elif key < node.key:
                node.left = _recurRemove(node.left, key)
            elif key > node.key:
                node.right = _recurRemove(node.right, key)
            return node
        
        self.root = _recurRemove(self.root, key)


    def getInorderKeys(self) -> List[int]:
        def _recurInorder(node, arr):
            if node == None:
                return
            _recurInorder(node.left, arr)
            arr.append(node.key)
            _recurInorder(node.right, arr)

        inOrderKeys = []
        _recurInorder(self.root, inOrderKeys)
        return inOrderKeys