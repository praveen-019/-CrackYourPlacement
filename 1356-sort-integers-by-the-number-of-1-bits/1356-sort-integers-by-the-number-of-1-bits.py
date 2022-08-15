class Solution(object):
    def sortByBits(self, arr):
        arr.sort()
        def bin(a):
            sum = 0
            while(a>0):
                sum = sum + a%2
                a = a/2
            return sum
        res = []
        for i in range(0,len(arr)):
            res.append(bin(arr[i]))

        result = []
        l = max(res) + 1
        for i in range(0,len(arr)):
            p = min(res)
            q = res.index(p) 
            result.append(arr[q])
            res[q] = l
        return result
   

        """
        result = {}
        for i in range(0,len(arr)):
            result[arr[i]] = res[i]
        print(result)
        
        p=sorted(result.items(), key =lambda kv:(kv[1], kv[0]))
        
        x = []
        for i in range(0,len(p)):
            x.append(p[i][0])
        return x
        
        :type arr: List[int]
        :rtype: List[int]
        """