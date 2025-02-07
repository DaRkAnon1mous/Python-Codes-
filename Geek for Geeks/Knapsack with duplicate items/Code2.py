#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        n = len(val)
        prev = [0]*(capacity+1)
        curr = [0]*(capacity+1)
        for i in range(1,n+1):
            for j in range(1,capacity+1):
                exclude = prev[j]
                include = 0
                if wt[i-1]<=j:
                    include = val[i-1]+curr[j-wt[i-1]]
                curr[j]= max(include,exclude)
            prev = curr[:]
        return curr[capacity]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
