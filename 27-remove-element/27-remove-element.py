class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        r = len(nums)
        while i < r:
            if nums[i] == val:
                nums[i] = nums[r-1]
                r -= 1
            else:
                i += 1
        return r