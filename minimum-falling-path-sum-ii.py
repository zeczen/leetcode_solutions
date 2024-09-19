# https://leetcode.com/problems/minimum-falling-path-sum-ii
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ma = mb = float('inf'),0
        ma1 = mb1 = float('inf'),0
        for j in range(N):
            if grid[-1][j] < ma[0]:
                mb = ma
                ma = (grid[-1][j],j)
            elif grid[-1][j] < mb[0]:
                mb = (grid[-1][j],j)
        for i in range(N-2,-1,-1):
            # print(ma,mb)
            for j in range(N):
                if ma[1] != j: grid[i][j] += ma[0]
                else: grid[i][j] += mb[0]
                if grid[i][j] < ma1[0]:
                    mb1 = ma1
                    ma1 = (grid[i][j],j)
                elif grid[i][j] < mb1[0]:
                    mb1 = (grid[i][j], j)

            ma,mb = ma1,mb1
            ma1 = mb1 = float('inf'),0
            # print(grid[i])
        return min(grid[0])
