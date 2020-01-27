Expr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

class Solution(object):
    def hasdigit(self, str_item):
        for i in str_item:
            if i.isdigit():
                return True
        return False
    
    def evalRPN(self, tokens):
        stack_expression = []
        for i in tokens:
            if self.hasdigit(i):
                stack_expression.append(int(i))
            else:
                op2 = stack_expression.pop()
                op1 = stack_expression.pop()
                if i == '+':
                    op = op1 + op2
                elif i == '-':
                    op = op1 - op2
                elif i == '*':
                    op = op1 * op2
                elif i == '/':
                    op = op1 / op2
                #print(str(op1) + i + str(op2))
                stack_expression.append(int(op))
        if len(stack_expression) == 1:
            print("yes")
            return stack_expression[0]

                


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(Expr))
