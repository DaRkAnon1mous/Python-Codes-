## Recursion Approach (last test case time limit exceed)
#User function Template for python3

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        n = len(val)
        def help(i,rem_w):
            if i >n-1 or rem_w==0:
                return 0
            exclude = help(i+1,rem_w)
            include = 0
            if wt[i]<=rem_w:
                include = val[i]+help(i+1,rem_w-wt[i])
            return max(exclude,include)
        return help(0,capacity)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read capacity
        capacity = int(input())
        values = list(map(
            int,
            input().strip().split()))  # Using 'values' instead of 'val'
        weights = list(map(
            int,
            input().strip().split()))  # Using 'weights' instead of 'wt'
        ob = Solution()
        print(ob.knapSack(capacity, values, weights))
        print("~")

# } Driver Code Ends
