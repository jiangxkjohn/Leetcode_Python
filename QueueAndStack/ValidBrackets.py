st = "()[]{}"


class Solution:
        
    def isValid(self, s: str) -> bool:
        self.stack = []
        for item in s:
            if item == ')' or item == ']' or item == '}' and self.stack != []:
                if self.judge(self.stack[-1], item):
                    self.stack.pop()
                else:
                    self.stack.append(item)
            else :
                self.stack.append(item)
        if self.stack == []:
            return True
        else:
            return False
        
    def judge(self, top, item):
        if item == ')' and top == '(':
            return True
        elif item == ']' and top == '[':
            return True
        elif item == '}' and top == '{':
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isValid(st))