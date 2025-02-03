## Tabulation Approach T=O(n) S=O(1) best time and space optimized
class Solution:
    def tribonacci(self, n: int) -> int:
        f0 = 0
        f1 = 1
        f2 = 1
        curr =0
        if n == 0:
            return f0
        if n==1 or n==2:
            return f1
        for i in range(3,n+1):
            curr = f0+f1+f2
            f0=f1
            f1 =f2
            f2 =curr
        return curr
