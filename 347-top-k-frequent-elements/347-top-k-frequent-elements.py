class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        nums.clear()
        d = sorted(d.items(),key = lambda item:item[1])
        d = d[::-1]
        for i in range(k):
            nums.append(d[i][0])
        return nums
        