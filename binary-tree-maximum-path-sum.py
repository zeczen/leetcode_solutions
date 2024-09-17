# https://leetcode.com/problems/binary-tree-maximum-path-sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def postorder(pos):
            
            if not pos.left and not pos.right: return pos.val
            a = b = float('-inf')
            if pos.left: a = postorder(pos.left)
            if pos.right: b = postorder(pos.right)

            mx = 0
            mn = 0
            if pos.right and pos.left: mx, mn = max(pos.right.val, pos.left.val), min(pos.right.val, pos.left.val)
            elif pos.right: mx = pos.right.val
            elif pos.left: mx = pos.left.val
            pos.val += max(mx, 0)
            return max(a, b, pos.val + mn, pos.val)
            
        return postorder(root)
