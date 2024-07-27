class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]* n for i in range (m)]
        for ind in indices:
            row = ind[0]
            col = ind[1]
            for i in range(n):
                matrix [row][i] +=1
            for i in range(m):
                matrix [i][col]+=1
        total_odd_nbr = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2 !=0:
                    total_odd_nbr +=1
        return total_odd_nbr
        