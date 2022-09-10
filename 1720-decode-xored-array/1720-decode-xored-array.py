class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = []
        decoded.append(first)
        for i in encoded:
            first = first^i
            decoded.append(first)
        return decoded
            