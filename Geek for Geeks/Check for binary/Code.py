# Return true if str is binary, else false
def isBinary(str):
    for char in str:
        if char not in ('0', '1'):
            return False
    return True


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends
