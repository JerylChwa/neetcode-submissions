class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operations:
                stack.append(token)
            elif token in operations:
                a = int(stack.pop())
                b = int(stack.pop())
                result = self.do(b, a, token)
                stack.append(result)
        
        return int(stack[0])

    
    def do(self, a: int, b: int, operation: str) -> int:
        if operation == "+":
            return a+b
        elif operation == "-":
            return a-b
        elif operation == "*":
            return a*b
        elif operation == "/":      
            return a/b
        else:
            return None