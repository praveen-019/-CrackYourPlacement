class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        n.sort()
        x = n[-1]*n[-2]*n[-3]
        if n[0] < 0:
            y = n[-1]*n[0]*n[1]
            return max(x,y)
        return x