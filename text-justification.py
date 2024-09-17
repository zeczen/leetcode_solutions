# https://leetcode.com/problems/text-justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        data = []

        N = len(words)
        k = 0
        while 1:
            line = []
            m = 0
            for i in range(k,N):
                if m + len(words[i]) + len(line)-1 >= maxWidth: break
                m += len(words[i])
                line.append(words[i])
            k += len(line)
            # m is length of chars
            spc = maxWidth-m 
            if k == N:
                break
            if len(line) == 1:
                data.append(line[0]+' ' * spc)
                continue

            lst = spc // (len(line)-1)
            frst = spc-lst*(len(line)-1)
            data.append((' '*lst+' ').join(line[:frst]+['']) + (' '*lst).join(line[frst:]))
        
        return data+[' '.join(line) + ' ' * (maxWidth-m-len(line)+1)]
