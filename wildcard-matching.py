# https://leetcode.com/problems/wildcard-matching

class State:
    def __init__(self):
        # self.acc = acc
        self.trans = {}  # [char] = set
        self.parent = {}  # [char] = set
    def transition(self, let):
        if let in self.trans:
            yield from self.trans[let]
        if let != '?' and '?' in self.trans: 
            yield from self.trans['?']
    def rev(self, let):
        if let in self.parent:
            yield from self.parent[let]
        if let != '?' and '?' in self.parent: 
            yield from self.parent['?']
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
        for i in range(N-1):
            if p[i+1] == '*' and p[i] in ('*','-'):
                p[i] = '-'
        for l in range(N):
            if p[l] == '-': continue
            if p[l] == '*': 
                tmp = State()
                tmp.addtrans('?', tmp)
                pos.addtrans('?', tmp)
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
        N = len(s)

        # # acc = pos
        # def dfs(state, i):
        #     if i == N:
        #         return state == pos
        #     # for st in state.epstrans():
        #     #     for stt in st.transition(s[i]):

        #     #         if any((dfs(sttt, i+1) for sttt in stt.epstrans())): return True
        #     return any((dfs(st,i+1) for st in state.transition(s[i])))
        # #
        # return any((dfs(s, 0) for s in start))
        Q1 = collections.deque([(s,-1) for s in start])  # from start
        v1 = set()
        Q2 = collections.deque([(pos, N)])  # from the end
        v2 = set()
        while Q1 and Q2:
            # print('Q1', Q1)
            # print('Q2', Q2)
            q1, i1 = Q1.popleft()
            if (q1,i1) not in v1:
                v1.add((q1, i1))
                if i1 != N-1: Q1.extend(((s,i1+1) for s in q1.transition(s[i1+1])))
            q2, i2 = Q2.popleft()
            if (q2,i2) not in v2:
                v2.add((q2, i2))
                if i2 != 0: Q2.extend(((s,i2-1) for s in q2.rev(s[i2-1])))
            if (q1, i1+1) in v2 or (q2, i2-1) in v1:
                # print((q1, N-i1), (q2, N-i2))
                # print(v1)
                # print(v2)
                return True
        while Q1:
            q1, i1 = Q1.popleft()
            if (q1, i1+1) in v2:
                return True
        while Q2:
            q2, i2 = Q2.popleft()
            if (q2, i2-1) in v1:
                return True

        return False
