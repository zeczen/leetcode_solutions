# https://leetcode.com/problems/n-queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        data = []
        def valid(x,y):
            for j in range(y):
                if board[j][x] == 'Q':
                    return False
            for i in range(1,min(x,y)+1):
                if board[y-i][x-i] == 'Q': 
                    return False
            for i in range(1,min(n-x,y+1)):
                if board[y-i][x+i] == 'Q': 
                    return False
            return True
    
        def dfs(row):
            if row == n:
                data.append([''.join(board[i]) for i in range(n)])
                return
            for i in range(n):
                if not valid(i,row): continue
                board[row][i] = 'Q'
                dfs(row+1)
                board[row][i] = '.'
        dfs(0)
        return data
