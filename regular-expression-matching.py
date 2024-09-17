# https://leetcode.com/problems/regular-expression-matching

class State:
    def __init__(self):
        self.trans = {}  # [char] = set
        self.parent = {}  # [char] = set
    def transition(self, let):
        if let in self.trans:
            yield from self.trans[let]
        if '.' in self.trans: 
            yield from self.trans['.']
    def rev(self, let):
        if let in self.parent:
            yield from self.parent[let]
        if '.' in self.parent: 
            yield from self.parent['.']

    # def epstrans(self):
    #     # traverse epsilon transisions
    #     Q = collections.deque([self])
    #     while Q:  # not supposed to be multiples yileds of the same one
    #         s = Q.popleft()
    #         yield s
    #         Q.extend(s.eps)

    def addtrans(self, let, nxt):
        if let in self.trans:
            self.trans[let].append(nxt)
        else: 
            self.trans[let] = [nxt]
        if let in nxt.parent:
            nxt.parent[let].append(self)
        else:
            nxt.parent[let] = [self]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pos = State()
        start = [pos]
        N = len(p)
        p = list(p)
        for i in range(N):
            if p[i] == '*' and p[i-1] == '.':
                for j in range(i-2,-1,-2):
                    if p[j] == '*':
                        p[j] = p[j-1] = '-'
                        continue
                    if p[j] != '-': break
                for j in range(i+1,N-1,2):
                    if p[j+1] == '*':
                        p[j] = p[j+1] = '-'
                        continue
                    else: break
                    if p[j] != '-': break
            elif i < N-2 and p[i] == p[i+2] == '*' and p[i-1] == p[i+1]:
                p[i] = p[i-1] = '-'
        for l in range(N-1):
            if p[l] == '-' or p[l] == '*': continue
            if p[l+1] == '*':
                tmp = State()
                tmp.addtrans(p[l], tmp)
                pos.addtrans(p[l], tmp)
                # register tmp on all the places
                for k, v in pos.parent.items():
                    # from state v there is a trans on char k
                    for st in v:
                        st.addtrans(k, tmp)
                if start[-1] == pos:
                    start.append(tmp)
                pos = tmp
                continue
            tmp = State()
            pos.addtrans(p[l], tmp)
            pos = tmp
        if p[-1] != '*' and p[-1] != '-':
            tmp = State()
            pos.addtrans(p[-1], tmp)
            pos = tmp
        acc = pos
        N = len(s)
        Q1 = collections.deque([(s,-1) for s in start])  # from start
        v1 = {(s,-1) for s in start}
        Q2 = collections.deque([(pos, N)])  # from the end
        v2 = {(pos, N)}
        while Q1 and Q2:
            q1, i1 = Q1.popleft()
            q2, i2 = Q2.popleft()

            v1.add((q1, i1))
            v2.add((q2, i2))
            if (q1, i1+1) in v2 or (q2, i2-1) in v1:
                return True

            if i1 != N-1: Q1.extend(((s,i1+1) for s in q1.transition(s[i1+1])))
            if i2 != 0: Q2.extend(((s,i2-1) for s in q2.rev(s[i2-1])))
        return False
        # N = len(s)
        # def dfs(state, i):
        #     if i == N:
        #         return state == acc
        #     # for st in state.epstrans():
        #     #     for stt in st.transition(s[i]):

        #     #         if any((dfs(sttt, i+1) for sttt in stt.epstrans())): return True
        #     return any((dfs(st,i+1) for st in state.transition(s[i])))
        # return any((dfs(s, 0) for s in start))
