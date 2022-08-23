class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n += 1
        l = []
        a = 0
        b = 0
        for i in range(1,n):
            if i%3 == 0:
                a = 1
            if i%5 == 0:
                b = 1
            if a == 1 and b == 1:
                l.append("FizzBuzz")
                a = 0
                b = 0
            elif a == 1:
                l.append("Fizz")
                a = 0
            elif b == 1:
                l.append("Buzz")
                b = 0
            else:
                l.append(str(i))
        return l