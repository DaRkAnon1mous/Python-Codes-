#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       left = 0  # Initialize the left pointer
       current_sum = 0  # This will store the current subarray sum
    
    # Iterate over the array with the right pointer
       for right in range(n):
            current_sum += arr[right]  # Add the current element to the sum
        
        # If current_sum exceeds the target, move the left pointer to reduce the window size
            while current_sum > s and left < right:
                current_sum -= arr[left]
                left += 1
        
        # If the current_sum matches the target, return the 1-based indices
            if current_sum == s:
                return (left + 1, right + 1)  # Return 1-based indexing
    
    # If no subarray is found that matches the target, return -1
       return [-1]

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
