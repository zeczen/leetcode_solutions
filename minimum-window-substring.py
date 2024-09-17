# https://leetcode.com/problems/minimum-window-substring
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = dict(Counter(t))
        N = len(t)
        n = N
        l = 0
        r = 0  # 1

        i, j = 0, len(s)+1
        while r < len(s):
            if s[r] in s_dict:
                s_dict[s[r]] -= 1
                if s_dict[s[r]] >= 0: n -= 1
            
            while n == 0:
                if s[l] not in s_dict:
                    l += 1
                elif s_dict[s[l]] < 0:
                    # not have impact
                    s_dict[s[l]] += 1
                    l += 1
                else:
                    # update m and preperare for next iter
                    if j-i > r-l: i, j = l, r
                    s_dict[s[l]] += 1
                    n += 1
                    l+=1
                    break
            r += 1
        return s[i:j+1] if j < len(s)+1 else ''
