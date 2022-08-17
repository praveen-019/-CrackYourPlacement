class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        temp = ""
        for i in words:
            for j in i:
                temp = temp + m[a.index(j)]
            res.append(temp)
            temp = ""
        r = []
        [r.append(x) for x in res if x not in r]
        return len(r)