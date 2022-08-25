class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        stack = ['(']
        count = 1
        for i in range(n):
            if s[i] == '(' and stack[-1] == '(':
                stack.append(s[i])
                if count < len(stack):
                    count += 1
            if s[i] == ')':
                stack.pop()
        return count-1