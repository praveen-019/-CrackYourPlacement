class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = float('inf')
        p = float('inf')
        for i in range(len(nums)):
            if(nums[i] == p):
                nums[i] = n
            else:
                p = nums[i]
        a = nums.count(n)
        for i in range(a):
            nums.remove(n)
            
        