## Approach 4 Space Optimisation Tabulation T=O(n) S=O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev,curr,counter = 0,1,1
        while counter <n:
            next = prev+curr
            counter+=1
            prev = curr
            curr = next
        return curr
