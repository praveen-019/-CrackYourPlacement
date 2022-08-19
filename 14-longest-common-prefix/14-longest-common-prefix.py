class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        for i in strs:
            if len(i) < l:
                l = len(i)
        count = ""
        for i in range(l):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return count
            count += strs[0][i]
        return count