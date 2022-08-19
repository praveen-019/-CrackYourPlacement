class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        a = []
        m = 0
        while r < len(s):
            if s[r] not in a:
                a.append(s[r])
                if (r-l+1)>m:
                    m = r-l+1
                r += 1
            else:
                a.remove(s[l])
                l += 1
        return m