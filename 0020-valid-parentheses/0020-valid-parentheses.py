class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif stack:
                o = stack.pop()
                if (c == ')' and o != '(') or (c == ']' and o != '[') or (c == '}' and o != '{'):
                    return False
            elif  c == ')' or c == ']' or c == '}':
                return False
        return not stack
                    
            