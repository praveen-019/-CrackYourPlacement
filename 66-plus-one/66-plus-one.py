class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(str(ele) for ele in digits))
        a = a + 1
        a = [int(ele) for ele in str(a)]
        return a