class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxsize = k + 1
        self.queue = list(range(self.maxsize))
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.maxsize
            self.queue[self.tail] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.maxsize
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.head+1)%self.maxsize]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.tail + 1) % self.maxsize == self.head:
            return True
        else:
            return False 

if __name__ == "__main__":
    s = MyCircularQueue(3)
    print(s.enQueue(1))
    print(s.enQueue(2))
    print(s.enQueue(3))
    print(s.enQueue(4))
    print(s.Rear())