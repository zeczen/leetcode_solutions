# https://leetcode.com/problems/unique-paths-iii
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        def ngh(x, y):
            if x != 0 and not grid[x-1][y]%2: yield x-1,y
            if x != N-1 and not grid[x+1][y]%2: yield x+1,y
            if y != 0 and not grid[x][y-1]%2: yield x,y-1
            if y != M-1 and not grid[x][y+1]%2: yield x,y+1

        def dfs(i, j, n):
            if grid[i][j] == 2 or n == 0: return grid[i][j] == 2 and n == 0
            s = 0
            grid[i][j] = -1
            for x,y in ngh(i, j):            
                s += dfs(x, y, n-1)
            grid[i][j] = 0
            return s

        i = j = None
        n = 1
        for x in range(N):
            for y in range(M):
                if grid[x][y] == 1:
                    i, j = x, y
                elif not grid[x][y]: n += 1
        return dfs(i, j, n)
