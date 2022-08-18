class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = []
        l.append(s[0])
        count = 0
        for i in range(1,len(s)):
            if len(l) > 0 and s[i] != l[-1]:
                l.pop()
            else:
                l.append(s[i])
            if len(l) == 0:
                count += 1
        return count