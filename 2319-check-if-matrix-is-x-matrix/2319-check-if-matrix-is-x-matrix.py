class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        # Diagonals
        
        col = len(grid[0])-1
        
        for i in range(len(grid)):
            if grid[i][i] == 0 or grid[i][col] == 0:
                return False
            col -= 1
        
        # Other Elements
        col = len(grid[0])-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i != j and j != col:
                    if grid[i][j] != 0:
                        return False
            col -= 1
    
        return True