class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = {'+': lambda a, b: a + b,'-': lambda a, b: a - b,'*': lambda a, b: a * b,'/': lambda a, b: int(a/b) }

        for i in range(len(tokens)):
            if tokens[i] in operations and len(stack) >= 2:
                b = int(stack.pop())
                a= int(stack.pop())
                result = operations[tokens[i]](a,b) 
                stack.append(result)
            else :
                stack.append(tokens[i])
        
        return int(stack[-1])
            
            

        