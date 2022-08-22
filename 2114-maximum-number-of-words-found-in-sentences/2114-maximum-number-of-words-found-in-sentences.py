class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = len(sentences)
        res = 0
        for i in range(n):
            temp = sentences[i].split(' ')
            if len(temp) > res:
                res = len(temp)
        return res