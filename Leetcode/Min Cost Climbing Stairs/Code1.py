## Recursion Approach  , Time limit Exceeded T=O(2^n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def help(i):
            if i>n-1:
                return 0
            onestep = cost[i]+help(i+1)
            twostep = cost[i]+help(i+2)
            return min(onestep,twostep)
        return min(help(0),help(1))
