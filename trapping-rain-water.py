# https://leetcode.com/problems/trapping-rain-water
class Solution:
    def trap(self, height: List[int]) -> int:
        
        s = 0
        l1 = 1
        r1 = len(height) - 2
        
        l = height[0]
        r = height[-1]
        
        while l1 <= r1:
            while l <= r and l1 <= r1:
                # advance l1
                l = max(l, height[l1])
                s += max(0, l - height[l1])
                l1 += 1
            while l > r and l1 <= r1:
                # advance r1
                r = max(r, height[r1])
                s += max(0, r - height[r1])
                r1 -= 1
    
        return s
