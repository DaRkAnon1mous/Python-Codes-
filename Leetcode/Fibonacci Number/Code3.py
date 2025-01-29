## Approach 3 Tabulatin (Iteration) T=O(n)
class Solution:
    def fib(self, n: int) -> int:
        dp=[0]*(n+1)
        if n>0:
            dp[1]=1
        count=1
        while(count<n):
            count+=1
            dp[count]=dp[count-1]+dp[count-2]
        return dp[n]
