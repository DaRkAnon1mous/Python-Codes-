##Approach 1 : T=O(n) S = O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        survivor = 0
        for i in range(2,n+1):
            survivor = (survivor+k)%i
        return survivor +1
