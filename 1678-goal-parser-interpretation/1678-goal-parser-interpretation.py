class Solution:
    def interpret(self, command: str) -> str:
        n = command.count('()')
        for i in range(n):
            command = command.replace('()','o')
        n = command.count('(al)')
        for i in range(n):
            command = command.replace('(al)','al')
        return command