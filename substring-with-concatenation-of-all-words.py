# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(words[0])
        w = Counter(words)

        n = []
        for i in range(len(s) +1- (N * len(words))):
                w1 = w.copy()
                for j in range(i, i + N*len(words), N):
                    if not w1.get(s[j:j+N]):
                        break
                    w1[s[j:j+N]] -= 1
                else:
                    n.append(i)
        return n
