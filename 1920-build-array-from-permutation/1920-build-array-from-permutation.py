class Solution(object):
    def buildArray(self, nums):
        res = []
        for i in range(0,len(nums)):
            res.append(nums[nums[i]])
        return res
        """
        :type nums: List[int]
        :rtype: List[int])
        """
        