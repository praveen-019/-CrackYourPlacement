class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        temp = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    for k in range(len(matrix)):
                        if(matrix[k][j] != 0):
                            matrix[k][j] = temp
                    for l in range(len(matrix[0])):
                        if(matrix[i][l] != 0):
                            matrix[i][l] = temp
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == temp:
                    matrix[i][j] = 0
        return matrix
            
        """
        Do not return anything, modify matrix in-place instead.
                    
        """
        