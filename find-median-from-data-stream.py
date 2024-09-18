# https://leetcode.com/problems/find-median-from-data-stream
class MedianFinder:

    def __init__(self):
        self.r = [float('inf')]
        self.l = [float('inf')]
        self.m = None
        self.N = 0

    def addNum(self, num: int) -> None:
        self.N += 1
        if self.N % 2:
            if self.r[0] < num:  # add to r
                self.m = heapq.heappushpop(self.r, num)
            else:
                self.m = -heapq.heappushpop(self.l, -num)
        else:
            mx = max(num, self.m)
            mn = min(num, self.m)
            heapq.heappush(self.r, mx)
            heapq.heappush(self.l, -mn)

    def findMedian(self) -> float:
        if self.N % 2:
            return self.m
        return (self.r[0] - self.l[0]) / 2
