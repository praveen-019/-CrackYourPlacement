class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        m = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                else:
                    if len(l) > m:
                        m = len(l)
                    l.clear()
                    break
        if len(s) == 1:
            return 1
        return m