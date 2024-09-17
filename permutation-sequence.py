# https://leetcode.com/problems/permutation-sequence
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = []
        nums = [str(i) for i in range(1,1+n)]
        k -= 1
        ln = n-1
        while k > 0:
            i = k // math.factorial(ln)
            k -= i*math.factorial(ln)
            ln -= 1
            # print(nums[i],i,ln)
            s.append(nums[i])
            nums.pop(i)  # O(n) <= O(9) = O(1)

        return ''.join(s+nums)
