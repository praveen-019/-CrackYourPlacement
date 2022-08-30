class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        temp = 0
        for x,y in boxTypes:
            if truckSize <= x:
                temp += truckSize*y
                break
            temp += x*y
            truckSize -= x
        return temp