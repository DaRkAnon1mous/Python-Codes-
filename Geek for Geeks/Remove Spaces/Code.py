#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        h=''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            else:
                h += s[i]
        return h

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends
