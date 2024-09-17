# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i < N:
            tmp = nums[i]

            if 1 <= nums[i] <= N and nums[i] != nums[tmp-1]: 
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
                continue
            i += 1

        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1
