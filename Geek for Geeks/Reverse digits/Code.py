#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		n1 = str(n)
		n1 = n1[::-1]
		n1 = int(n1)
		return n1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends
