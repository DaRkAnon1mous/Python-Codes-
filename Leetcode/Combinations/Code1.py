## Approach 1 with less optimisation
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def help(i,comb):
            if len(comb)==k:
                res.append(comb[:])
                return
            for j in range(i,n+1):
                comb.append(j)
                help(j+1,comb)
                comb.pop()
        help(1,[])
        return res
