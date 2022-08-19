class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        l.append(0)
        for i in s:
            if((l[-1] == '(' and i == ')') or (l[-1] == '[' and i == ']') or (l[-1] == '{' and i == '}')):
                l.pop()
            else:
                l.append(i)
        return len(l)==1