# https://leetcode.com/problems/minimum-replacements-to-sort-the-array
from math import ceil

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i+1] < nums[i]:
                k = ceil(nums[i] / nums[i+1])
                counter += k - 1
                nums[i] //= k
        return counter
