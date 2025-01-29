## Approach 2 Memoization (recursion with storing) using Hash Table T=O(n)
class Solution:
    def fib(self, n: int) -> int:
        ht = {0: 0,1: 1}
        if n in ht:
            return ht[n]
        else:
            ht[n] = self.fib(n-1)+self.fib(n-2)
            return ht[n]
