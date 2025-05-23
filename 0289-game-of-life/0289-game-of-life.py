class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[ (1,0), (0, 1), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        toChange=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbour = 0
                for direction in directions:
                    nr, nc = direction[0]+i, direction[1]+j
                    if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]):
                        if board[nr][nc] ==1:
                            neighbour+=1
                if board[i][j] == 1 and neighbour < 2:
                    toChange.append((i,j))
                if board[i][j] ==1 and neighbour > 3:
                    toChange.append((i,j))
                if board[i][j] == 0 and neighbour == 3:
                    toChange.append((i,j))

        for r,c in toChange:
            board[r][c] = 1 if board[r][c]==0 else 0