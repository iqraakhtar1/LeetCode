class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l= len(matrix)
        for i in range(l):
            for j in range(i, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        
       
    