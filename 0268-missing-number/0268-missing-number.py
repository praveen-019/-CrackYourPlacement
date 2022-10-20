class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = 1
        n = len(nums) + 1
        for i in range(n):
            if i not in dict:
                return i