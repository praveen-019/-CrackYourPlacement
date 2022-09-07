class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        n = int(math.sqrt(num)) + 1
        if num == 1:
            return False
        res = 0
        for i in range(1,n):
            if num%i == 0:
                res += i + num//i
        return (res-num) == num
        