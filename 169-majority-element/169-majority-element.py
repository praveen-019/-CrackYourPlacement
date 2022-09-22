class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        n = len(nums)//2
        for i in nums:
            if dict[i] > n:
                return i
            
        