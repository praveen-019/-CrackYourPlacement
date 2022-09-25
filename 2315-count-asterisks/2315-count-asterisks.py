class Solution:
    def countAsterisks(self, s: str) -> int:
        l = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '|':
                if l == 0:
                    l = 1
                elif l == 1:
                    l = 0
            elif l == 0 and s[i] == '*':
                count += 1
        return count