# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        idxs = [0 for _ in range(len(nums))]
        pqn = [(nums[i][0], i) for i in range(len(nums))]
        
        for i in range(len(nums)):
            nums[i].append(float('inf'))

        pqx = max(pqn)[0]
        heapq.heapify(pqn)

        rng = pqn[0][0], pqx
        val = 0
        while val != float('inf'):
            _, i = pqn[0] 
            idxs[i] += 1
            val = nums[i][idxs[i]]
            heapq.heappushpop(pqn, (val, i))
            pqx = max(pqx, val)
            rng = min(rng, (pqn[0][0], pqx), key=lambda a: a[1]-a[0])

        return rng
