## Approach 2: T=O(n) S = O(n)
def findTheWinner(n, k):
    def josephus(n):
        if n == 1:
            return 0  
        #recursive case
        return (josephus(n-1) + k) % n
    return josephus(n)
