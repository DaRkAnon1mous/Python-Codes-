##Approach 1 : T=O(n) S = O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        survivor = 0
        for i in range(2,n+1):
            survivor = (survivor+k)%i
        return survivor +1

## Approach 2: T=O(n) S = O(n)
def findTheWinner(n, k):
    def josephus(n):
        if n == 1:
            return 0  
        #recursive case
        return (josephus(n-1) + k) % n
    return josephus(n)



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
