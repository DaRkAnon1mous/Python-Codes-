## Approach 3: T=O(n^2) S=O(n)
def findTheWinner(n, k):
    #write code here
    arr = [i+1 for i in range(n)]
    def func(arr, start):
        if len(arr)==1:
            return arr[0]
        index_remove = (start+(k-1)) % len(arr)
        del arr[index_remove]
        return func(arr,index_remove)


    return func(arr,0)
