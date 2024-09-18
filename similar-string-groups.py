# https://leetcode.com/problems/similar-string-groups
class Solution:    
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a: str, b: str) -> bool:        
            idx = len(a)
            for i in range(len(a)):
                if a[i] != b[i]:
                    idx = i
                    break
            else: return True
            for j in range(idx+1, len(a)):
                if a[j] != b[j]:
                    if a[idx] != b[j] or a[j] != b[idx]:
                        return False
                    else:
                        idx = j
                        break
            else: return False
            return a[idx+1:] == b[idx+1:]
        
        def dfs(i):
            s = strs[i]
            strs[i] = ""
            
            for j in range(len(strs)):
                if strs[j] and similar(s, strs[j]):
                    dfs(j)      
        
        counter = 0
        for i in range(len(strs)):
            if strs[i]:
                counter += 1
                dfs(i)
                    
        return counter
            
