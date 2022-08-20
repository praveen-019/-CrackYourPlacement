class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        m = {}
        n = 0
        while r < len(s):
            if s[r] not in m:
                m[s[r]] = r
                if (r-l+1) > n:
                    n = (r-l+1)
                r += 1
            else:
                if l <= m[s[r]]:
                    l = m[s[r]] + 1
                m[s[r]] = r
                if (r-l+1) > n:
                    n = (r-l+1)
                r += 1
        return n
                