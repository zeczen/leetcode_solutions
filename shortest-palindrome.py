# https://leetcode.com/problems/shortest-palindrome
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        for i in range(len(s)-1,-1,-1):
            # does i/2 can be the middle for the pali?
            j = 0
            n = i // 2
            while j <= n and s[n-j] == s[n+j+(i%2)]:
                j += 1
              
            if j > n:
                return s[:n+j+(i%2)-1:-1] + s
        return s
