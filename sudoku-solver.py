# https://leetcode.com/problems/sudoku-solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def get_nigh(x, y):
            s = set()
            for i in range(x):  # vertical - 
                yield (i,y)
            for i in range(x+1,9):
                yield (i,y)
            for j in range(y):  # horizontal |
                yield (x,j)
            for j in range(y+1,9):
                yield (x,j)
            xbx, ybx = x // 3 * 3, y // 3 * 3
            for i in range(x % 3):
                for j in range(y % 3):
                    yield (xbx+i,ybx+j)
                for j in range(y % 3+1, 3):
                    yield (xbx+i,ybx+j)
            for i in range(x % 3+1,3):
                for j in range(y % 3):
                    yield (xbx+i,ybx+j)
                for j in range(y % 3+1, 3):
                    yield (xbx+i,ybx+j)
            # xbx, ybx = x // 3 * 3, y // 3 * 3
            # return {(i,y) for i in range(9)}.union( 
            #     {(x,j) for j in range(9)}).union( 
            #     {(xbx, ybx+j) for j in range(3)}).union(  # box
            #     {(xbx+1, ybx+j) for j in range(3)}).union(
            #     {(xbx+2, ybx+j) for j in range(3)})
        nums = {'1','2','3','4','5','6','7','8','9'}
        for x,y in itertools.product(range(9), range(9)):
            if board[x][y] == '.':
                board[x][y] = nums - {board[i][j] for i,j in get_nigh(x,y) if type(board[i][j]) == str}
        def dfs():
            x,y = min(((len(board[i][j]),i,j) for i,j in itertools.product(range(9), range(9)) if type(board[i][j]) == set), default=(123))[1:]
            vals = board[x][y]
            for val in vals:
                updated = []
                board[x][y] = val
                for i,j in get_nigh(x,y):
                    if type(board[i][j]) == set and val in board[i][j]:
                        board[i][j] -= {val}
                        updated.append((i,j))
                dfs()  # recursive call
                for i,j in updated:
                    print(board[i][j])
                    board[i][j].add(val)
                board[x][y] = vals
        try: dfs()
        except TypeError: pass
