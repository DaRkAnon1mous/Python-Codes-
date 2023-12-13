

class Solution:
    def missingNumber(self,array,n):
        var1 = (n * (n + 1)) // 2
        var2 = sum(array)
        num = var1 - var2

        return num


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends
