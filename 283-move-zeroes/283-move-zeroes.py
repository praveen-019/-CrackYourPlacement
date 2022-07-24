class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            pass
        else:
            n = nums.count(0)
            for i in range(n):
                nums.remove(0)
                nums.append(0)
                        
        """
        Do not return anything, modify nums in-place instead.
        """
        