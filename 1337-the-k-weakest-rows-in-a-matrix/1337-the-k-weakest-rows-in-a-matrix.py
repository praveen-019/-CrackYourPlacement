class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap = []
        n = len(mat)
        for i in range(n):
            minHeap.append([mat[i].count(1),i])
        
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            x,y = heapq.heappop(minHeap)
            res.append(y)
        return res
    