class Solution:
    def DFS(self, array, result):
        if len(array) == len(self.nums):
            if result == self.S:
                self.cout += 1
                # print(array)
                return None
            else:
                return None
        else:
            if self.nums[len(array)] == 0:
                array.append(0)
                self.DFS([e for e in array], result)
                # self.factor = self.factor * 2
                # print(self.factor, array)
            else:
                array.append(1)
                self.DFS([e for e in array], result + self.nums[len(array)-1] * array[-1])
                array[-1] = -1
                self.DFS([e for e in array], result + self.nums[len(array)-1] * array[-1])
        
    def findTargetSumWays(self, nums, S: int) -> int:
        array = []
        self.cout = 0
        self.nums = nums
        self.S = S
        self.factor = 1
        self.DFS(array, 0)
        for item in self.nums:
            if item == 0:
                self.cout = self.cout * 2
        return self.cout

if __name__ == "__main__":
    s = Solution()
    nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
    S = 35
    print(s.findTargetSumWays(nums, S))