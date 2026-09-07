import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={ '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.truediv
                    }
        stack=[]
        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[i](a,b)
                if i == '/':
                    result = int(result)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]    

        