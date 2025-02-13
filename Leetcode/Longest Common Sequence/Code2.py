## Memoization (takes more time)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp=[[-1]*(m) for _ in range(n)]
        def help(i1,i2):
            if i1>n-1 or i2 > m-1:
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if text1[i1]==text2[i2]:
                dp[i1][i2] =1+help(i1+1,i2+1)
                return dp[i1][i2]
            dp[i1][i2]= max(help(i1,i2+1),help(i1+1,i2))
            return dp[i1][i2]
        return help(0,0)
