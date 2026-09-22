class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dArray = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.dArray[i]


    def set(self, i: int, n: int) -> None:
        self.dArray[i] = n

    def pushback(self, n: int) -> None:
        if len(self.dArray) == self.capacity:
            self.resize()
        self.dArray.append(n)

    def popback(self) -> int:
        return self.dArray.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.dArray)
        
    def getCapacity(self) -> int:
        return self.capacity
