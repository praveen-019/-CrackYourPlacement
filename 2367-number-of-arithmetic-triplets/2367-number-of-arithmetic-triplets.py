class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        count = 0
        for i in nums:
            if (i+diff) in nums and (i+(diff*2)) in nums:
                count += 1
        return count