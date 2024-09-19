# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        Q = collections.deque()
        
        n = 0  # #of k-flip
        for i in range(N-k+1):
            if Q and Q[0] == i: Q.popleft()
            if nums[i] ^ (len(Q) % 2): continue

            # perform k-flip
            Q.append(i+k)
            n += 1
        for i in range(N-k, N):
            if Q and Q[0] == i: Q.popleft()
            if not (nums[i] ^ (len(Q) % 2)): return -1 
        return n

# Q%2 n[i]
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
