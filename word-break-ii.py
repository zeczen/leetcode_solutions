# https://leetcode.com/problems/word-break-ii
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def foo(s, a=0):
            if a >= len(s):
                return [s]

            possible = []
            for i in range(a, len(s)+1):
                if s[a:i] in wordDict:
                    space_s = ' '.join([s[:i], s[i:]])
                    possible += foo(space_s, i + 1)

            return possible
        return list(map(lambda x: x[:-1], foo(list(s))))
