class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = len(jewels)
        res = 0
        for i in range(len(jewels)):
            res += stones.count(jewels[i])
        return res