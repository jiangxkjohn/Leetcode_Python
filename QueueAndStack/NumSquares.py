class Solution:
    def Initial(self, num):
        self.maxsize = num + 1
        self.queue = list(range(self.maxsize))
        self.head = 0
        self.tail = 0
        self.hashmap = [0] * self.n
        
    def enQueue(self, value) -> bool:
        if self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.maxsize
            self.queue[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.maxsize
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.head+1)%self.maxsize]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.maxsize == self.head:
            return True
        else:
            return False  

    def numSquares(self, n: int) -> int:
        self.n = n
        self.Initial(n)
        self.enQueue(n)
        self.mark = self.tail
        self.times = 0
        while not self.isEmpty():
            if self.next_node(self.Front()):
                return self.times + 1
            if self.mark == (self.head + 1) % self.maxsize:
                self.mark = self.tail
                self.times = self.times + 1
            self.deQueue()
        return -1
        
    def next_node(self, node):
        for num_square in range(1, int(self.n**0.5)+1):
            next = node - num_square ** 2
            if next == 0:
                return True
            if next > 0 and self.hashmap[next] == 0:
                self.enQueue(next)
                self.hashmap[next] = 1

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(112))
