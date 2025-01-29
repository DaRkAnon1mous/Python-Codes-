## Highest Time complexity of O(2^n) and irrelavant recusrive iteration
class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
