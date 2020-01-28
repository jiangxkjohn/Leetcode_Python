

class Solution:

    def Initial(self, num):
        self.maxsize = num + 1
        self.queue = list(range(self.maxsize))
        self.head = 0
        self.tail = 0
        
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

    def numIslands(self, grid):
        if grid == []:
            return 0
        self.grid = grid
        self.x_len = len(grid)
        self.y_len = len(grid[0])
        self.hasbeenread = [([0] * self.y_len) for i in range(self.x_len)]
        self.islandnum = 0
        for x in range(self.x_len):
            for y in range(self.y_len):
                if self.hasbeenread[x][y] == 1 or self.grid[x][y] == '0':
                    pass
                else:
                    self.Initial(self.x_len*self.y_len)
                    self.islandnum = self.islandnum + 1
                    self.traverse(x, y)
        return self.islandnum

    def traverse(self, x, y):
        self.enQueue([x, y])
        self.hasbeenread[x][y] = 1
        while not self.isEmpty():
            next_node = self.find_next_node(self.Front())
            self.deQueue()
            if not(next_node == []): 
                for item in next_node:
                    self.enQueue(item)
                

    def find_next_node(self, parent_node):
        x = parent_node[0]
        y = parent_node[1]
        next_node = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]
        result = []
        for item in next_node:
            if self.isvalid(item):
                result.append(item)
                self.hasbeenread[item[0]][item[1]] = 1
        return result

    def isvalid(self, node):
        if node[0] < 0 or node[0] > self.x_len-1:
            return False
        if node[1] < 0 or node[1] > self.y_len-1:
            return False
        if self.hasbeenread[node[0]][node[1]] == 1:
            return False
        if self.grid[node[0]][node[1]] == '0':
            return False
        return True

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    grid = [['1']]
    s = Solution()
    print(s.numIslands(grid))