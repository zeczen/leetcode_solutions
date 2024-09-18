# https://leetcode.com/problems/swim-in-rising-water
  class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        Q = [(0, 0,0)]
        N,M = len(grid),len(grid[0])

        def get_nigh(x,y):
            if x != 0: yield x-1,y
            if y != 0: yield x,y-1
            if x != M-1: yield x+1,y
            if y != N-1: yield x,y+1

        m = grid[0][0]
        while Q:
            v,x,y = heapq.heappop(Q)
            
            m = max(m, v)
            
            if x == M-1 and y == N-1: return m
            for nx,ny in get_nigh(x,y):
                if grid[ny][nx] != -1: 
                    heapq.heappush(Q, (grid[ny][nx],nx,ny))
                    grid[ny][nx] = -1
