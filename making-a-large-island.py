# https://leetcode.com/problems/making-a-large-island
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        def get_ngh(i, j):
            if i+1 < N: yield i+1, j
            if j+1 < M: yield i, j+1
            if i > 0: yield i-1, j
            if j > 0: yield i, j-1
        
        # clac islands
        sizes = [0, -1]
        def dfs(i, j, n):
            grid[i][j] = n
            s = 1
            for a, b in get_ngh(i, j):
                if grid[a][b] == 1:
                    s += dfs(a, b, n)
            return s
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    sizes.append(dfs(i, j, len(sizes)))

        # find 0
        return max(((1+reduce(lambda a,b: a+sizes[b], set(grid[a][b] for a,b in get_ngh(i, j)), 0)) for i, j in product(range(N), range(M)) if grid[i][j] == 0), default=N*M)
