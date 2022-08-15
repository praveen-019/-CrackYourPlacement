class Solution(object):
    def restoreString(self, s, indices):
        n = len(s)
        arr = [0]*n
        for i in range(0,n):
            arr[indices[i]] = s[i]
        return ''.join(arr)
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        