# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed
class RandomizedCollection:
    R = 0.5
    def __init__(self):
        self.d = {}
        self.a = []
        self.n = 0

    def insert(self, val: int) -> bool:
        self.d[val] = self.d.get(val, 0) + 1
        self.a.append((val, self.d[val]))
        self.n += 1
        return self.d[val] == 1

    def remove(self, val: int) -> bool:
        if not self.d.get(val, 0): return False
        self.d[val] -= 1
        self.n -= 1

        if len(self.a) / (self.n+1) < self.R:
            self.a = [-1 for _ in range(self.n)]
            i = 0
            # build arr
            for k, v in self.d.items():
                for j in range(v):
                    self.a[i] = (k, j)
                    i += 1
        return True
    def getRandom(self) -> int:
        k, v = random.choice(self.a)
        while self.d[k] < v:
            k, v = random.choice(self.a)
        return k
