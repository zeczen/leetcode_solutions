# https://leetcode.com/problems/distinct-subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M,N = len(s),len(t)
        dp = [[0 for j in range(M)] for i in range(N)]

        dp[-1][-1] = int(s[-1] == t[-1])
        for j in range(M-2,-1,-1):
            dp[-1][j] = dp[-1][j+1] + (s[j] == t[-1])

        for i in range(N-2,-1,-1):
            for j in range(M-2,-1,-1):
                dp[i][j] = dp[i][j+1] + (s[j] == t[i]) * dp[i+1][j+1]
        return dp[0][0]
