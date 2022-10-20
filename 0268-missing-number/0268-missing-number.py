class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = []
        for i in range(n+1):
            l.append(i)
        for i in l:
            if i not in nums:
                return i