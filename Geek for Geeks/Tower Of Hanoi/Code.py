# User function Template for python3

class Solution:
    
    def  towerOfHanoi(self, n, fromm, to, aux):
        # Your code here
        count = 0
        def helper(N,fromm,to,aux):
            nonlocal count
            if N==1:
                count+=1
                #print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
                return
            helper(N-1,fromm,aux,to)
            count+=1
            #print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))

            helper(N-1,aux,to,fromm)
        helper(N,fromm,to,aux)  
        return count

#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.towerOfHanoi(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
