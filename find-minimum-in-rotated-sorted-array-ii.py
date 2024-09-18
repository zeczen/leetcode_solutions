# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        def foo(a,b):
            if a +1 >= b: 
                yield min(nums[a],nums[b])
                return
            m = (a+b) // 2
            while not nums[(m+1) % N] > nums[m] < nums[m-1]:
                yield nums[m]
                if nums[m] < nums[b]:
                    b = m
                elif nums[m] > nums[b]:
                    a = m+1
                else:
                    if nums[a] != nums[m]:
                        b = m
                    else: 
                        f1 = foo(a,m)
                        f2 = foo(m,b)
                        for l1,l2 in zip(f1,f2):
                            if l1 != l2: break
                        if l1 < l2: 
                            yield l1
                            yield from f1
                        else:
                            yield l2 
                            yield from f2
                        return
        
                m = (a+b) // 2
    
            yield nums[m]
        *_,last = foo(0,N-1)
        return last
