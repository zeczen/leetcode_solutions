# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def brouteapproach(a, b, n, odd):
            def mymin(a, i, k):
                if i == len(a):
                    return k
                return min(a[i], k)
            # both sorted, unknown length
            i, j = 0, 0
            while n > i + j:
                if i < len(a) and (j == len(b) or a[i] < b[j]):
                      i += 1
                else: j += 1
            if odd: return mymin(b, j, a[i]) if i < len(a) else b[j]
            else: 
                if i == len(a): return (b[j]+b[j+1]) / 2
                if j == len(b): return (a[i]+a[i+1]) / 2
                return (a[i] + mymin(a, i+1, b[j])) / 2 if a[i] < b[j] else (b[j] + mymin(b, j+1, a[i])) / 2
        # SUCCESS
        _, a = max((len(nums1), nums1), (len(nums2), nums2))
        _, b = min((len(nums1), nums1), (len(nums2), nums2))
        inf = max(a[-1], b[-1])+1 if len(b) else a[-1]+1
        minf = min(a[0], b[0])-1 if len(b) else a[0]-1
        blr = (len(a) - len(b)) // 2
        odd = ((len(a) % 2) + (len(b) % 2)) % 2  ## TODO: adjust (as function of blr?)
        n = 0  # count how many been truncated, from left considering the both arrays
        l1, r1 = 0, len(a)-1
        l2, r2 = 0, len(b)-1 + blr + blr+(odd)  # r2 + odd == r1

      while (r2-l2) + (r1-l1) > 25:  # can be adjestment
            m1 = l1 + ((r1-l1+1) // 2)
            m2 = l2 + ((r2-l2) // 2)
            # if a[m1] < getb(m2)
            if (a[m1] < minf and m2 < blr) or (a[m1] < inf and blr + len(b) <= m2) or (blr <= m2 < len(b)+blr and a[m1] < b[m2-blr]): 
                n += m1-l1
                l1 = m1 
                r2 = m2
            else:
                n += max(m2-max(l2, blr), 0)
                r1 = m1
                l2 = m2

        return brouteapproach(a[l1:r1+1], b[max(0, l2-blr):r2+1-blr], ((len(a) + len(b) -1) // 2)-n, odd)
