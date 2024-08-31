#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        sumi= 0

        while n>0:
            d = n%10
            sumi =sumi + d
            n = n//10
        
        
        n1 = str(sumi)
        c= n1[::-1]
        if n1 == c:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends
