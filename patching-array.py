# https://leetcode.com/problems/patching-array
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ret = 0
        if nums[0] != 1:
            nums.insert(0,1)
            ret += 1
        last = 1
        i = 1
        if len(nums) < 2: 
            nums.append(2)
            ret += 1
        num = nums[1]
        j = 2
        
        while j < n+1:
            if j >= num:  j = last+num+1
            if j >= n+1: break
            if last == j-1 or i == len(nums)-1:
                num = last+1
                ret += 1
                i -= 1  # next time grab the same num
            else:
                i += 1
                num = nums[i]
            last = j-1                
        return ret
