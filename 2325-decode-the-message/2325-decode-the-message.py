class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        key = [ele for ele in key if ele != " "]
        k = []
        [k.append(ele) for ele in key if ele not in k]
        res = []
        for i in message:
            if i in k:
                res.append(l[k.index(i)])
            else:
                res.append(i)
        return "".join(res)