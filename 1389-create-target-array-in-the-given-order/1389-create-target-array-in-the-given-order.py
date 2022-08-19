class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        def add(ind,ele):
            for i in range(ind,len(l)):
                l[i],ele = ele,l[i]
            l.append(ele)
        for i in range(len(nums)):
            add(index[i],nums[i])
        return l