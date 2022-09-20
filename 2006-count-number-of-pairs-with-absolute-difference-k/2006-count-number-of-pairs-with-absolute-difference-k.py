class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashlist = [0]*201
        for i in nums:
            hashlist[i] += 1
        return sum(hashlist[i + k] for i in nums)