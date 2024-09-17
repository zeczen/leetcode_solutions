# https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/1233038529/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [-1] + heights + [-1]

        tmp = [0]  # increasing order stack
        resl = []
        for i in range(1, len(heights)-1):
            if heights[tmp[-1]] < heights[i]:
                resl.append(tmp[-1])
                tmp.append(i)
            else:
                while heights[tmp[-1]] >= heights[i]:
                    tmp.pop()
                resl.append(tmp[-1])
                tmp.append(i)
                
        resr = []
        tmp = [len(heights)-1]  # increasing order stack
        for i in range(len(heights)-2, 0, -1):
            if heights[tmp[-1]] < heights[i]:
                resr.append(tmp[-1])
                tmp.append(i)
            else:
                while heights[tmp[-1]] >= heights[i]:
                    tmp.pop()
                resr.append(tmp[-1])
                tmp.append(i)

        return max([heights[i] * (resr[-i] - resl[i-1]-1) for i in range(1, len(heights)-1)])
