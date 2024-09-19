# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        N = len(traversal)
        i = 0
        matches = re.finditer(r'\d+', traversal)
        c = None
        def dfs(i, pos, d):
            nonlocal c
            try:
                curr = next(matches)
                if curr.start() - i == d:  # child
                    if not pos.left:
                        pos.left, i = dfs(curr.end(), TreeNode(int(curr.group())), d+1)
                        if not c:
                            curr = next(matches)
                        else:
                            curr = c
                            c = None
                        if curr.start() - i == d:
                            pos.right, i = dfs(curr.end(), TreeNode(int(curr.group())), d+1)
                        elif curr.start() - i < d:  c = curr  # push curr to the iterator
                elif curr.start() - i < d:  # up on the stack
                    c = curr  # push curr to the iterator
                return pos, i
            except StopIteration:
                return pos, N
        curr = next(matches)
        i = curr.end()
        return dfs(i, TreeNode(int(curr.group())), 1)[0]
            
