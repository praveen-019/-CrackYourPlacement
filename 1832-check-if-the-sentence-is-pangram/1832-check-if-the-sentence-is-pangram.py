class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = 'qwertyuiopasdfghjklzxcvbnm'
        l = []
        [l.append(ele) for ele in sentence if ele not in l]
        for i in range(26):
            if c[i] not in l:
                return False
        return True
        
        