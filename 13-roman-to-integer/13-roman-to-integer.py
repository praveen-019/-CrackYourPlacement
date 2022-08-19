class Solution:
    def romanToInt(self, s: str) -> int:
        s = [ele for ele in s][::-1]
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]] < d[s[i-1]]:
                count -= d[s[i]]
            else:
                count += d[s[i]]
        return count