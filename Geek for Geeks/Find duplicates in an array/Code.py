class Solution:
    def duplicates(self, arr, n): 
    	if not arr:
            return [-1]

        counts = {}
        duplicates = []

        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            if count > 1:
                duplicates.append(num)

        if not duplicates:
            return [-1]
        else:
            return sorted(duplicates)
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
