class Solution:
    def frequencySort(self, s: str) -> str:
        s = [ele for ele in s]
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        res = ""
        d = sorted(d.items(),key=lambda item:item[1])
        for i in d[::-1]:
            res = res + i[0]*i[1]
        return res