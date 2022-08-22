class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = ''
        n = len(address)
        for i in range(n):
            if address[i] == '.':
                l += '[.]'
            else:
                l += address[i]
        return l
        