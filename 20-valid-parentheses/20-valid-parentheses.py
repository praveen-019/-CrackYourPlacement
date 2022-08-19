class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(0)
        for i in s:
            if((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}')):
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==1