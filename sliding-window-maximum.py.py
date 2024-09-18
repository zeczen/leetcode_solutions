# https://leetcode.com/problems/sliding-window-maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(Q)
    
        arr = [0] * (len(nums) - k+1)
        for i in range(len(nums) - k):
            arr[i] = -Q[0][0]
            while Q and Q[0][1] <= i:
                heapq.heappop(Q)
            heapq.heappush(Q, (-nums[i+k], i+k))
        arr[-1] = -(Q[0][0])
        return arr
