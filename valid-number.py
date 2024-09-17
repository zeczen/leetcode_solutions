# https://leetcode.com/problems/valid-number
class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        if s[i] in ['-', '+']:
            i += 1
        if i == len(s) or not s[i].isdigit() and s[i] != '.': return False
        dot = False
        while i < len(s):
            if s[i].isdigit():
                i += 1
            elif s[i].lower() ==  'e':
                i += 1
                if i < len(s) and s[i] in ['+', '-']:
                    i += 1
                return i < len(s) and s[i:].isdigit()
            elif s[i] == '.' and not dot:
                i += 1
                dot = True
                if i == len(s): return i >= 3 or s[0] not in ['+', '-', '.']
                if not s[i].isdigit() and (s[i].lower() != 'e' or not (s[0] in ['-', '+'] and s[1].isdigit() or s[0].isdigit())): return False
            else:
                return False
        return True
