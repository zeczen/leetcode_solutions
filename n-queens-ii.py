# https://leetcode.com/problems/n-queens-ii
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        data = 0
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
                nonlocal data
                data += 1
                return
            for i in range(n):
                if not valid(i,row): continue
                board[row][i] = 'Q'
                dfs(row+1)
                board[row][i] = '.'
        dfs(0)
        return data
