class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)//2
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        d = sorted(d.items(),key=lambda item:item[1])[::-1]
        sum = 0
        count = 1
        for i in d:
            sum += i[1]
            if len(arr)-sum <= n:
                break
            count += 1
        return count