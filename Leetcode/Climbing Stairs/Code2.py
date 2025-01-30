## Final Approach T=O(n) S= O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2 :
            return n
        prev = 1
        curr = 2
        counter = 2
        while counter <n:
            next = prev+curr
            counter+=1
            prev = curr
            curr = next
        return curr
