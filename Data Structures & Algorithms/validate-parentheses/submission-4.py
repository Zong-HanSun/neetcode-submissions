class Solution:
    def isValid(self, s: str) -> bool:
        str_list = list(s)

        if len(str_list) % 2 != 0:
            return False
        
        stack = []

        for char in str_list:
            if char == '(':
                stack.append(char)
            if char == '[':
                stack.append(char)
            if char == '{':
                stack.append(char)
            
            if char == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()

            if char == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()

            if char == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()



        return len(stack) == 0
            

            


        