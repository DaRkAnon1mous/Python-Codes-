class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        def help(i1,i2):
            if i1>n-1 or i2 > m-1:
                return 0
            if text1[i1]==text2[i2]:
                return 1+help(i1+1,i2+1)
            return max(help(i1,i2+1),help(i1+1,i2))
        return help(0,0)
