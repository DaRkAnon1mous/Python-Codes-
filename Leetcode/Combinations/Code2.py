class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def help(i,comb):
            if len(comb)==k:
                res.append(comb[:])
                return
            need = k-len(comb) ## Optimisation
            for j in range(i,n-(need-1)+1):
                comb.append(j)
                help(j+1,comb)
                comb.pop()
        help(1,[])
        return res
