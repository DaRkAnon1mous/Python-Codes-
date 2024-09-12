#User function Template for python3
class Solution:
    # Just print the space seperated array elements
	def printArray(self, arr):
	    l= len(arr)
	    for i in range(l):
	        print(arr[i] , end=' ')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.printArray(arr)
        print()
        tc = tc - 1

# } Driver Code Ends
