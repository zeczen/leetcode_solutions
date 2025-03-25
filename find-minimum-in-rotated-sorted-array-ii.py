# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dfs(l,r):
            while r-l > 2:
                m = (l+r) // 2
                # print(l, m, r)
                if nums[l] < nums[m] < nums[r]:    # 1 2 3
                    return nums[l]
                elif nums[r] < nums[l] < nums[m]:  # 2 3 1
                    l = m+1
                elif nums[m] < nums[r] < nums[l]:  # 3 1 2
                    r = m-1
                    if nums[r] > nums[m]: return nums[m]
                elif nums[l] == nums[m] < nums[r]: # 1 1 2
                    r = m-1
                elif nums[r] == nums[m] < nums[l]: # 2 1 1
                    r = m-1
                    if nums[r] > nums[m]: return nums[m]
                elif nums[l] == nums[r] < nums[m]: # 1 2 1
                    l = m+1
                elif nums[m] == nums[r] > nums[l]: # 1 2 2
                    r = m-1
                elif nums[l] == nums[r] > nums[m]: # 2 1 2
                    r = m-1
                    if nums[r] > nums[m]: return nums[m]
                elif nums[m] == nums[l] > nums[r]: # 2 2 1
                    l = m+1
                elif nums[l] == nums[m] == nums[r]:# 1 1 1
                    return min(dfs(l,m-1), dfs(m+1,r))
            return min(nums[l:r+1])
        return dfs(0, len(nums)-1)
