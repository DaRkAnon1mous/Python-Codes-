
class Solution:
	def find_median(self, v):
		v.sort()
		m = 0
		l = len(v)
		if l%2 == 0:
		    m = (v[(l//2) - 1] + v[l//2]) //2

		else:
		    m = v[l//2]
		    
		return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
