# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])

        def dfs(i, j, val):
            m = 0
            if i != 0:
                if type(matrix[i-1][j]) == tuple:
                    if val < matrix[i-1][j][0]:
                        m = max(m, matrix[i-1][j][-1]+1) 
                elif val < matrix[i-1][j]:
                    dfs(i-1, j, matrix[i-1][j])
                    m = max(m, matrix[i-1][j][-1]+1) 
            if i != N-1:
                if type(matrix[i+1][j]) == tuple:
                    if val < matrix[i+1][j][0]:
                        m = max(m, matrix[i+1][j][-1]+1) 
                elif val < matrix[i+1][j]:
                    dfs(i+1, j, matrix[i+1][j])
                    m = max(m, matrix[i+1][j][-1]+1) 

            if j != 0:
                if type(matrix[i][j-1]) == tuple:
                    if val < matrix[i][j-1][0]:
                        m = max(m, matrix[i][j-1][-1]+1) 
                elif val < matrix[i][j-1]:
                    dfs(i, j-1, matrix[i][j-1])
                    m = max(m, matrix[i][j-1][-1]+1) 

            if j != M-1:
                if type(matrix[i][j+1]) == tuple:
                    if val < matrix[i][j+1][0]:
                        m = max(m, matrix[i][j+1][-1]+1) 
                elif val < matrix[i][j+1]:
                    dfs(i, j+1, matrix[i][j+1])
                    m = max(m, matrix[i][j+1][-1]+1)
            matrix[i][j] = (matrix[i][j], m)
        
        m = -1
        for i in range(N):
            for j in range(M):
                if type(matrix[i][j]) == int: dfs(i, j, matrix[i][j])
                m = max(m, matrix[i][j][-1])
        return m+1
