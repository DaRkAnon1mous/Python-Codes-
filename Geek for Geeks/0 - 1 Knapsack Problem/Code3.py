## Tabulation Approach Complxity same as Code2
#User function Template for python3

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        n= len(val)
        dp = [[0]* (capacity+1) for _ in range(n+1)]
        for i in range (1, n+1):
            for j in range(1, capacity+1):
                exclude = dp[i-1][j]
                include = 0
                if wt[i-1]<=j:
                    include = val[i-1]+dp[i-1][j-wt[i-1]]
                dp [i][j] = max(exclude, include)
        return dp[n][capacity]


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
