class Solution(object):
    def numIdenticalPairs(self, nums):
        res = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    res += 1
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        