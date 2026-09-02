class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif c == '*':
                result = int(stack.pop()) * int(stack.pop())
                stack.append(result)
            elif c == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                result = int(b/a)
                stack.append(result)
            elif c == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                result = b - a
                stack.append(result)
            else:
                stack.append(int(c))
        
        return stack[-1]
                