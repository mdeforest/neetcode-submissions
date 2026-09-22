class LinkedListNode:
    def __init__(self, value: int, nextNode: LinkedListNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.firstNode = None
        
    def get(self, index: int) -> int:
        currentNode = self.firstNode
        i = 0
        while i != index and currentNode:
            currentNode = currentNode.nextNode
            i += 1

        if i == index and currentNode:
            return currentNode.value

        return -1

    def insertHead(self, val: int) -> None:
        oldNode = self.firstNode
        self.firstNode = LinkedListNode(val, oldNode)
        print(self.getValues())        

    def insertTail(self, val: int) -> None:
        currentNode = self.firstNode
        previousNode = None
        if not currentNode:
            self.firstNode = LinkedListNode(val)
            return

        while currentNode:
            previousNode = currentNode
            currentNode = currentNode.nextNode  
            
        currentNode = LinkedListNode(val)
        previousNode.nextNode = currentNode
        print(self.getValues())      

    def remove(self, index: int) -> bool:
        currentNode = self.firstNode
        previousNode = None
        i = 0

        if i == index and currentNode:
            self.firstNode = currentNode.nextNode
            return True

        while i != index and currentNode.nextNode:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            i += 1
        
        if i == index and currentNode:
            previousNode.nextNode = currentNode.nextNode
            print(self.getValues())
            return True

        return False
        

    def getValues(self) -> List[int]:
        if not self.firstNode:
            return []

        allValues = []
        currentNode = self.firstNode

        while currentNode:
            allValues.append(currentNode.value)
            currentNode = currentNode.nextNode

        return allValues
        
