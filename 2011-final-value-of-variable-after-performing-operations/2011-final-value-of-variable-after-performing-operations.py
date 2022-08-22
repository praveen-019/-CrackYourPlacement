class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        x = 0
        for i in range(n):
            if operations[i] == '--X' or operations[i] == 'X--':
                x -= 1
            if operations[i] == '++X' or operations[i] == 'X++':
                x += 1
        return x