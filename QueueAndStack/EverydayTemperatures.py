temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
class Solution:
    def dailyTemperatures(self, T):
        self.stack = []
        ans = []
        for i in range(len(T)-1, -1, -1):
            while self.stack and T[i]>=T[self.stack[-1]]:
                self.stack.pop()
            if self.stack:
                ans.append(self.stack[-1] - i)
            else:
                ans.append(0)
            self.stack.append(i)
        ans.reverse()
        return ans

if __name__ == "__main__":
    t = Solution()
    print(t.dailyTemperatures(temperatures))