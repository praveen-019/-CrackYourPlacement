class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c = '0'
        def addBin(i,j):
            if i == '0' and j == '0':
                return ('0','0')
            if i == '1' and j == '1':
                return ('0','1')
            if (i == '0' and j == '1') or (i == '1' and j == '0'):
                return ('1','0')
        n = min(len(a),len(b))
        r = ''
        for i in range(n):
            t1 = addBin(a[i],b[i])
            t2 = addBin(t1[0],c)
            r += t2[0]
            c = str(max(int(t1[1]),int(t2[1])))
        if len(a) > len(b):
            m = len(a)
            for j in range(i+1,m):
                t2 = addBin(a[j],c)
                r += t2[0]
                c = t2[1]
        if len(b) > len(a):
            m = len(b)
            for j in range(i+1,m):
                t2 = addBin(b[j],c)
                c = t2[1]
                r += t2[0] 
        if c == '1':
            r += c
        return r[::-1]